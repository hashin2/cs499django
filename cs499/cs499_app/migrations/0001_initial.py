# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MotionEvent'
        db.create_table('cs499_app_motionevent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_x', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('event_y', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('time', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('cs499_app', ['MotionEvent'])

        # Adding model 'Parser'
        db.create_table('cs499_app_parser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('point_x', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('point_y', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pt_time', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('cs499_app', ['Parser'])

        # Adding model 'LoginUsers'
        db.create_table('cs499_app_loginusers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('cs499_app', ['LoginUsers'])

        # Adding model 'UserFiles'
        db.create_table('cs499_app_userfiles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numFiles', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('cs499_app', ['UserFiles'])


    def backwards(self, orm):
        # Deleting model 'MotionEvent'
        db.delete_table('cs499_app_motionevent')

        # Deleting model 'Parser'
        db.delete_table('cs499_app_parser')

        # Deleting model 'LoginUsers'
        db.delete_table('cs499_app_loginusers')

        # Deleting model 'UserFiles'
        db.delete_table('cs499_app_userfiles')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numFiles': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['cs499_app']