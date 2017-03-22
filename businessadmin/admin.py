'''j'''
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin,GroupAdmin
from .madmin import MultiDBModelAdmin
from .models import Localestringresource,InventoryUpdate
from django.contrib.auth.models import User,Group
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import TokenAdmin


'''class LocalestringresourceAdmin(MultiDBModelAdmin):
    list_display = ['id', 'resourcename', 'resourcevalue']
    using = 'gcgcommerce' 
    '''
class BusinessAdmin(AdminSite):
    site_header = 'Business Admin'
    # site_title = 'Admin Site'
    # index_title = 'Admin Site'

admin_site = BusinessAdmin(name='myadmin')


class InventoryUpdateAdmin(MultiDBModelAdmin):
    list_display = ['Name', 'ManufacturerPartNumber', 'StockQuantity', 'UnitPrice', 'VendorPrice', 'UnitsPerCase', 'PriceMeasure']
    using = 'gcgcommerce'

#admin.site.register(Localestringresource, LocalestringresourceAdmin)
#admin.site.register(InventoryUpdate, InventoryUpdateAdmin)
admin_site.register(Token, TokenAdmin)
admin_site.register(User,UserAdmin)
admin_site.register(Group,GroupAdmin)
admin_site.register(InventoryUpdate, InventoryUpdateAdmin)
