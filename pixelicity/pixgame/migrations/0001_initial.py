# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Locations'
        db.create_table(u'pixgame_locations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('centerLat', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('centerLng', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('locName', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('locType', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('locImage', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('locId', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pixgame', ['Locations'])

        # Adding model 'UserLocs'
        db.create_table(u'pixgame_userlocs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'pixgame', ['UserLocs'])

        # Adding M2M table for field locations on 'UserLocs'
        db.create_table(u'pixgame_userlocs_locations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userlocs', models.ForeignKey(orm[u'pixgame.userlocs'], null=False)),
            ('locations', models.ForeignKey(orm[u'pixgame.locations'], null=False))
        ))
        db.create_unique(u'pixgame_userlocs_locations', ['userlocs_id', 'locations_id'])


    def backwards(self, orm):
        # Deleting model 'Locations'
        db.delete_table(u'pixgame_locations')

        # Deleting model 'UserLocs'
        db.delete_table(u'pixgame_userlocs')

        # Removing M2M table for field locations on 'UserLocs'
        db.delete_table('pixgame_userlocs_locations')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pixgame.locations': {
            'Meta': {'object_name': 'Locations'},
            'centerLat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'centerLng': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locId': ('django.db.models.fields.IntegerField', [], {}),
            'locImage': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'locName': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'locType': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'pixgame.userlocs': {
            'Meta': {'object_name': 'UserLocs'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pixgame.Locations']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['pixgame']