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
            ('serial', self.gf('django.db.models.fields.CharField')(default='0', unique=True, max_length=50)),
            ('version', self.gf('django.db.models.fields.CharField')(default='0', max_length=30)),
            ('screenHeight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('screenWidth', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('cs499_app', ['Device'])

        # Adding model 'App'
        db.create_table('cs499_app_app', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('cs499_app', ['App'])

        # Adding model 'Session'
        db.create_table('cs499_app_session', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cs499_app.Device'])),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cs499_app.App'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('submission', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cs499_app', ['Session'])

        # Adding model 'MotionEvent'
        db.create_table('cs499_app_motionevent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('deviceId', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('downTime', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('edgeFlags', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('eventTime', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('metaState', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pressure', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('x', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('xPrecision', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('y', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('yPrecision', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('sessionId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cs499_app.Session'])),
        ))
        db.send_create_signal('cs499_app', ['MotionEvent'])


    def backwards(self, orm):
        # Deleting model 'Device'
        db.delete_table('cs499_app_device')

        # Deleting model 'App'
        db.delete_table('cs499_app_app')

        # Deleting model 'Session'
        db.delete_table('cs499_app_session')

        # Deleting model 'MotionEvent'
        db.delete_table('cs499_app_motionevent')


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
        'cs499_app.app': {
            'Meta': {'object_name': 'App'},
            'appname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cs499_app.device': {
            'Meta': {'object_name': 'Device'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'screenHeight': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'screenWidth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'serial': ('django.db.models.fields.CharField', [], {'default': "'0'", 'unique': 'True', 'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '30'})
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
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cs499_app.App']"}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cs499_app.Device']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submission': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['cs499_app']