# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Productos'
        db.create_table('app_productos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cantidad', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('app', ['Productos'])


    def backwards(self, orm):
        # Deleting model 'Productos'
        db.delete_table('app_productos')


    models = {
        'app.productos': {
            'Meta': {'object_name': 'Productos'},
            'cantidad': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'codigo': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['app']