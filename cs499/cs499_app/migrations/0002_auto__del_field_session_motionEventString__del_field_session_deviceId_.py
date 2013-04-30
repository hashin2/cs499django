# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Session.motionEventString'
        db.delete_column('cs499_app_session', 'motionEventString')

        # Deleting field 'Session.deviceId'
        db.delete_column('cs499_app_session', 'deviceId_id')

        # Deleting field 'Device.IMEI'
        db.delete_column('cs499_app_device', 'IMEI')

        # Deleting field 'Device.model'
        db.delete_column('cs499_app_device', 'model')

        # Adding field 'Device.serial'
        db.add_column('cs499_app_device', 'serial',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=50),
                      keep_default=False)

        # Adding field 'Device.version'
        db.add_column('cs499_app_device', 'version',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=30),
                      keep_default=False)

        # Adding field 'Device.screenHeight'
        db.add_column('cs499_app_device', 'screenHeight',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Device.screenWidth'
        db.add_column('cs499_app_device', 'screenWidth',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Session.motionEventString'
        db.add_column('cs499_app_session', 'motionEventString',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Session.deviceId'
        db.add_column('cs499_app_session', 'deviceId',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['cs499_app.Device']),
                      keep_default=False)

        # Adding field 'Device.IMEI'
        db.add_column('cs499_app_device', 'IMEI',
                      self.gf('django.db.models.fields.CharField')(default='imei number', max_length=50),
                      keep_default=False)

        # Adding field 'Device.model'
        db.add_column('cs499_app_device', 'model',
                      self.gf('django.db.models.fields.CharField')(default=' Model n/a', max_length=30),
                      keep_default=False)

        # Deleting field 'Device.serial'
        db.delete_column('cs499_app_device', 'serial')

        # Deleting field 'Device.version'
        db.delete_column('cs499_app_device', 'version')

        # Deleting field 'Device.screenHeight'
        db.delete_column('cs499_app_device', 'screenHeight')

        # Deleting field 'Device.screenWidth'
        db.delete_column('cs499_app_device', 'screenWidth')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cs499_app.device': {
            'Meta': {'object_name': 'Device'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'screenHeight': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'screenWidth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'serial': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '50'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '30'})
        },
        'cs499_app.files': {
            'Meta': {'object_name': 'Files'},
            'filename': ('django.db.models.fields.CharField', [], {'default': "'defaultFilename'", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cs499_app.motionevent': {
            'Meta': {'object_name': 'MotionEvent'},
            'action': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'deviceId': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'downTime': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'edgeFlags': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'eventTime': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metaState': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pressure': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sessionId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cs499_app.Session']"}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'xPrecision': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'yPrecision': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'cs499_app.session': {
            'Meta': {'object_name': 'Session'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cs499_app.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "'heatmap_auth_user'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['cs499_app']