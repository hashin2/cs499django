# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Device'
        db.create_table('cs499_app_device', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('IMEI', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('Model', self.gf('django.db.models.fields.CharField')(default=' Model n/a', max_length=30)),
        ))
        db.send_create_signal('cs499_app', ['Device'])

        # Adding model 'Session'
        db.create_table('cs499_app_session', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('DeviceId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cs499_app.Device'])),
            ('User', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cs499_app.LoginUsers'])),
            ('MotionEventId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cs499_app.MotionEvent'])),
            ('SubmissionTime', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 3, 19, 0, 0))),
        ))
        db.send_create_signal('cs499_app', ['Session'])

        # Adding unique constraint on 'LoginUsers', fields ['username']
        db.create_unique('cs499_app_loginusers', ['username'])

        # Deleting field 'UserFiles.user_id'
        db.delete_column('cs499_app_userfiles', 'user_id')

        # Adding field 'UserFiles.userId'
        db.add_column('cs499_app_userfiles', 'userId',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'MotionEvent.pressure'
        db.add_column('cs499_app_motionevent', 'pressure',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


        # Changing field 'MotionEvent.time'
        db.alter_column('cs499_app_motionevent', 'time', self.gf('django.db.models.fields.CharField')(max_length=30))

    def backwards(self, orm):
        # Removing unique constraint on 'LoginUsers', fields ['username']
        db.delete_unique('cs499_app_loginusers', ['username'])

        # Deleting model 'Device'
        db.delete_table('cs499_app_device')

        # Deleting model 'Session'
        db.delete_table('cs499_app_session')

        # Adding field 'UserFiles.user_id'
        db.add_column('cs499_app_userfiles', 'user_id',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=20),
                      keep_default=False)

        # Deleting field 'UserFiles.userId'
        db.delete_column('cs499_app_userfiles', 'userId')

        # Deleting field 'MotionEvent.pressure'
        db.delete_column('cs499_app_motionevent', 'pressure')


        # Changing field 'MotionEvent.time'
        db.alter_column('cs499_app_motionevent', 'time', self.gf('django.db.models.fields.IntegerField')())

    models = {
        'cs499_app.device': {
            'IMEI': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'Meta': {'object_name': 'Device'},
            'Model': ('django.db.models.fields.CharField', [], {'default': "' Model n/a'", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cs499_app.loginusers': {
            'Meta': {'object_name': 'LoginUsers'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'cs499_app.motionevent': {
            'Meta': {'object_name': 'MotionEvent'},
            'event_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'event_y': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pressure': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'time': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '30'})
        },
        'cs499_app.parser': {
            'Meta': {'object_name': 'Parser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'point_y': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pt_time': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'cs499_app.session': {
            'DeviceId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cs499_app.Device']"}),
            'Meta': {'object_name': 'Session'},
            'MotionEventId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cs499_app.MotionEvent']"}),
            'SubmissionTime': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 3, 19, 0, 0)'}),
            'User': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cs499_app.LoginUsers']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cs499_app.userfiles': {
            'Meta': {'object_name': 'UserFiles'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': "'40'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numFiles': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'userId': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['cs499_app']