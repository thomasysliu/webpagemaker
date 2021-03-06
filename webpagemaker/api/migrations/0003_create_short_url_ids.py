# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

NUMERALS = "Zv0w2x4y6z8AaBcCeDgEiFkGmHoIqJsKuL3M7NbOfPjQnRrS1T9UhVpW5XlYdt"

def rebase(num, numerals=NUMERALS):
    base = len(numerals)
    left_digits = num // base
    if left_digits == 0:
        return numerals[num % base]
    else:
        return rebase(left_digits, numerals) + numerals[num % base]

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."

        for user in orm.Page.objects.all():
            user.short_url_id = rebase(user.id)
            user.save()

    def backwards(self, orm):
        "Write your backwards methods here."

        for user in orm.Page.objects.all():
            user.short_url_id = ''
            user.save()

    models = {
        'api.page': {
            'Meta': {'object_name': 'Page'},
            'html': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'short_url_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['api']
    symmetrical = True
