# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Productos', fields ['codigo']
        db.create_unique('app_productos', ['codigo'])


    def backwards(self, orm):
        # Removing unique constraint on 'Productos', fields ['codigo']
        db.delete_unique('app_productos', ['codigo'])


    models = {
        'app.productos': {
            'Meta': {'object_name': 'Productos'},
            'cantidad': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'codigo': ('django.db.models.fields.PositiveSmallIntegerField', [], {'unique': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['app']