'''j'''
from django.contrib import admin
from .madmin import MultiDBModelAdmin
from .models import Localestringresource,InventoryUpdate


class LocalestringresourceAdmin(MultiDBModelAdmin):
    list_display = ['id', 'resourcename', 'resourcevalue']
    using = 'gcgcommerce'

class InventoryUpdateAdmin(MultiDBModelAdmin):
    list_display = ['Name', 'ManufacturerPartNumber', 'UnitPrice', 'VendorPrice', 'UnitsPerCase', 'PriceMeasure']
    using = 'gcgcommerce'

#admin.site.register(Localestringresource, LocalestringresourceAdmin)
#admin.site.register(InventoryUpdate, InventoryUpdateAdmin)
admin.site.register(InventoryUpdate, InventoryUpdateAdmin)
