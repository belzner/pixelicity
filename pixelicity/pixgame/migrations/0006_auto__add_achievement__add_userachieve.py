# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Achievement'
        db.create_table(u'pixgame_achievement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compName', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('humanName', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('hint', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'pixgame', ['Achievement'])

        # Adding model 'UserAchieve'
        db.create_table(u'pixgame_userachieve', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'pixgame', ['UserAchieve'])

        # Adding M2M table for field achievements on 'UserAchieve'
        db.create_table(u'pixgame_userachieve_achievements', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userachieve', models.ForeignKey(orm[u'pixgame.userachieve'], null=False)),
            ('achievement', models.ForeignKey(orm[u'pixgame.achievement'], null=False))
        ))
        db.create_unique(u'pixgame_userachieve_achievements', ['userachieve_id', 'achievement_id'])


    def backwards(self, orm):
        # Deleting model 'Achievement'
        db.delete_table(u'pixgame_achievement')

        # Deleting model 'UserAchieve'
        db.delete_table(u'pixgame_userachieve')

        # Removing M2M table for field achievements on 'UserAchieve'
        db.delete_table('pixgame_userachieve_achievements')


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
        u'pixgame.achievement': {
            'Meta': {'object_name': 'Achievement'},
            'compName': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'hint': ('django.db.models.fields.TextField', [], {}),
            'humanName': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '40'})
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
        u'pixgame.userachieve': {
            'Meta': {'object_name': 'UserAchieve'},
            'achievements': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pixgame.Achievement']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'pixgame.userlocs': {
            'Meta': {'object_name': 'UserLocs'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pixgame.Locations']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['pixgame']