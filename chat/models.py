# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Udn(models.Model):
    title = models.CharField(max_length=2000, blank=True, null=True)
    link = models.CharField(max_length=2000, blank=True, null=True)
    report = models.CharField(max_length=2000, blank=True, null=True)
    content = models.CharField(max_length=2000, blank=True, null=True)
    time = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        app_label = 'chat'
        managed = False
        db_table = 'udn'
