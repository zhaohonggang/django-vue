'''j'''
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin,GroupAdmin
from .madmin import MultiDBModelAdmin
from .models import Localestringresource,InventoryUpdate
from django.contrib.auth.models import User,Group
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import TokenAdmin
from django.utils.translation import gettext_lazy as _
from django.db.models import F
from django.db import connections

'''class LocalestringresourceAdmin(MultiDBModelAdmin):
    list_display = ['id', 'resourcename', 'resourcevalue']
    using = 'gcgcommerce' 
    '''
class BusinessAdmin(AdminSite):
    site_header = 'Business Admin'
    # site_title = 'Admin Site'
    # index_title = 'Admin Site'

admin_site = BusinessAdmin(name='businessadmin')

class InStockFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('In Stock')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'StockQuantity'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('True', _('Yes')),
            ('False', _('No')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'True':
            return queryset.filter(StockQuantity__gt = 0)
        elif self.value() == 'False':
            return queryset.filter(StockQuantity__lte = 0)
        else:
            return queryset

def run_usp_UpdatePricesWeekly(modeladmin, request, queryset):
    with connections['gcgcommerce'].cursor() as cursor:
        cursor.execute('EXEC [dbo].[usp_UpdatePricesWeekly]')
run_usp_UpdatePricesWeekly.short_description = "exec usp_UpdatePricesWeekly"

def toggle_Published(modeladmin, request, queryset):
    # s = queryset.filter(Published__exact = '1')
    s = ','.join(str(o.id) for o in queryset) 
    s = "UPDATE {0} SET Published = 1 - Published WHERE id in ({1})".format(queryset.model._meta.db_table, s)
    # InventoryUpdate.objects.raw('SELECT id, first_name FROM myapp_person'):
    with connections['gcgcommerce'].cursor() as cursor:
        cursor.execute(s)

    # queryset.filter(Published__exact = 1).update(Published=False)
    # queryset.filter(Published__exact = 0).update(Published=True)
    '''for o in queryset:
        s = o
    s = queryset.update(Published=bool(1- int(bool(F('Published'))))).query
    print(s)'''
toggle_Published.short_description = "Toggle selected items' published"

class InventoryUpdateAdmin(MultiDBModelAdmin):
    actions = [toggle_Published,run_usp_UpdatePricesWeekly]
    search_fields = ['Name','ManufacturerPartNumber']
    list_filter = ('Published',InStockFilter)
    readonly_fields = ('CasePrice',)
    list_display = ['Name', 'ManufacturerPartNumber', 'StockQuantity', 'VendorPrice', 'UnitPrice', 'PriceMeasure', 'UnitsPerCase', 'CasePrice','Published']
    using = 'gcgcommerce'
    def save_model(self, request, obj, form, change):
            obj.CasePrice = obj.UnitPrice * obj.UnitsPerCase
            obj.save()
#admin.site.register(Localestringresource, LocalestringresourceAdmin)
#admin.site.register(InventoryUpdate, InventoryUpdateAdmin)
admin_site.register(Token, TokenAdmin)
admin_site.register(User,UserAdmin)
admin_site.register(Group,GroupAdmin)
admin_site.register(InventoryUpdate, InventoryUpdateAdmin)
