# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AbcClient(models.Model):
    abc_client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    company_address = models.ForeignKey('Address', models.DO_NOTHING, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'abc_client'


class AbcResource(models.Model):
    abc_resource_id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey('Inventory', models.DO_NOTHING)
    resource_type = models.ForeignKey('ResourceType', models.DO_NOTHING)
    resource_name = models.CharField(max_length=45)
    max_number_of_resources = models.BigIntegerField()
    current_number_of_resources = models.BigIntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'abc_resource'


class AccessLog(models.Model):
    access_log_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=45)
    action = models.CharField(max_length=45)
    table_name = models.CharField(max_length=45, blank=True, null=True)
    field_name = models.CharField(max_length=45, blank=True, null=True)
    screen_name = models.CharField(max_length=45, blank=True, null=True)
    log_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'access_log'


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=45)
    postal_code = models.CharField(max_length=45)
    city = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'address'


class ClientContacts(models.Model):
    client_contacts_id = models.AutoField(primary_key=True)
    abc_client = models.ForeignKey(AbcClient, models.DO_NOTHING)
    contact = models.ForeignKey('Contact', models.DO_NOTHING)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client_contacts'


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    email_address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contact'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    abc_client = models.ForeignKey(AbcClient, models.DO_NOTHING)
    inventory_name = models.CharField(max_length=45)
    storage_type = models.ForeignKey('StorageType', models.DO_NOTHING)
    max_item_capacity = models.BigIntegerField()
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventory'


class ResourceType(models.Model):
    resource_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resource_type'


class StorageType(models.Model):
    storage_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'storage_type'
