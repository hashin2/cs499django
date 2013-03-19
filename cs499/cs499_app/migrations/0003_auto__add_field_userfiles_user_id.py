# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserFiles.user_id'
        db.add_column('cs499_app_userfiles', 'user_id',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 3, 7, 0, 0), max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserFiles.user_id'
        db.delete_column('cs499_app_userfiles', 'user_id')


    models = {
        'cs499_app.loginusers': {
            'Meta': {'object_name': 'LoginUsers'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'cs499_app.motionevent': {
            'Meta': {'object_name': 'MotionEvent'},
            'event_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'event_y': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'cs499_app.parser': {
            'Meta': {'object_name': 'Parser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'point_y': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pt_time': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'cs499_app.userfiles': {
            'Meta': {'object_name': 'UserFiles'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': "'40'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numFiles': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['cs499_app']