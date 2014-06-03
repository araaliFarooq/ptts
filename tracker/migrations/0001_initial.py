# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Route'
        db.create_table('tracker_route', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('route_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('route_start', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('route_end', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('tracker', ['Route'])

        # Adding model 'Bus'
        db.create_table('tracker_bus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('license_number', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracker.Route'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('tracker', ['Bus'])

        # Adding model 'Route_Stop'
        db.create_table('tracker_route_stop', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stop_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracker.Route'])),
        ))
        db.send_create_signal('tracker', ['Route_Stop'])

        # Adding model 'coordinate'
        db.create_table('tracker_coordinate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imei', self.gf('django.db.models.fields.IntegerField')()),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('tracker', ['coordinate'])

        # Adding model 'Contact'
        db.create_table('tracker_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tracker', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Route'
        db.delete_table('tracker_route')

        # Deleting model 'Bus'
        db.delete_table('tracker_bus')

        # Deleting model 'Route_Stop'
        db.delete_table('tracker_route_stop')

        # Deleting model 'coordinate'
        db.delete_table('tracker_coordinate')

        # Deleting model 'Contact'
        db.delete_table('tracker_contact')


    models = {
        'tracker.bus': {
            'Meta': {'object_name': 'Bus'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tracker.Route']"})
        },
        'tracker.contact': {
            'Meta': {'object_name': 'Contact'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tracker.coordinate': {
            'Meta': {'object_name': 'coordinate'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imei': ('django.db.models.fields.IntegerField', [], {}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'tracker.route': {
            'Meta': {'object_name': 'Route'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route_end': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'route_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'route_start': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'tracker.route_stop': {
            'Meta': {'object_name': 'Route_Stop'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tracker.Route']"}),
            'stop_name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['tracker']