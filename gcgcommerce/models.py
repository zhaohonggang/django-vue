# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Language(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)
    # Field name made lowercase.
    languageculture = models.CharField(
        db_column='LanguageCulture', max_length=20)
    # Field name made lowercase.
    uniqueseocode = models.CharField(
        db_column='UniqueSeoCode', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    flagimagefilename = models.CharField(
        db_column='FlagImageFileName', max_length=50, blank=True, null=True)
    rtl = models.BooleanField(db_column='Rtl')  # Field name made lowercase.
    # Field name made lowercase.
    limitedtostores = models.BooleanField(db_column='LimitedToStores')
    # Field name made lowercase.
    defaultcurrencyid = models.IntegerField(db_column='DefaultCurrencyId')
    # Field name made lowercase.
    published = models.BooleanField(db_column='Published')
    # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder')

    class Meta:
        managed = False
        db_table = 'Language'


class Localestringresource(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    languageid = models.ForeignKey(Language, db_column='LanguageId')
    # Field name made lowercase.
    resourcename = models.CharField(db_column='ResourceName', max_length=200)
    # Field name made lowercase.
    resourcevalue = models.TextField(db_column='ResourceValue')

    class Meta:
        managed = False
        db_table = 'LocaleStringResource'

class InventoryUpdate(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    Name = models.CharField(db_column='Name', max_length=400)
    ManufacturerPartNumber = models.CharField(db_column='ManufacturerPartNumber', max_length=400)
    ManageInventoryMethodId = models.IntegerField(db_column='ManageInventoryMethodId', default = 0)
    StockQuantity = models.IntegerField(db_column='StockQuantity', default=1000)
    UnitPrice = models.DecimalField(db_column='UnitPrice', max_digits=18, decimal_places=4) 
    VendorPrice = models.DecimalField(db_column='VendorPrice', max_digits=18, decimal_places=4) 
    UnitsPerCase = models.DecimalField(db_column='UnitsPerCase', max_digits=18, decimal_places=4, default=20) 
    PriceMeasure = models.CharField(db_column='PriceMeasure', max_length=400, default='kg')
    VendorId = models.IntegerField(db_column='VendorId', default=103)
    GCGBatchId = models.IntegerField(db_column='GCGBatchId', default=91)
    published = models.BooleanField(db_column='Published', default=True)
   
    class Meta:
        managed = False
        db_table = 'Inventory_update'
