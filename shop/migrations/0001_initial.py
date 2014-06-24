# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carousel'
        db.create_table('shop_carousel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('name_de', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('description_de', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('description_ru', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('shop', ['Carousel'])

        # Adding model 'Plan'
        db.create_table('shop_plan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('description_de', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('description_ru', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('options', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('options_ru', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('options_de', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=(), blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('shop', ['Plan'])

        # Adding model 'Feature'
        db.create_table('shop_feature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('name_de', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('html_class', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('description_de', self.gf('django.db.models.fields.TextField')(default='')),
            ('description_ru', self.gf('django.db.models.fields.TextField')(default='')),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('shop', ['Feature'])

        # Adding model 'FeaturePlugin'
        db.create_table('cmsplugin_featureplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('feature1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins1', to=orm['shop.Feature'])),
            ('feature2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins2', to=orm['shop.Feature'])),
            ('feature3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins3', to=orm['shop.Feature'])),
        ))
        db.send_create_signal('shop', ['FeaturePlugin'])

        # Adding model 'Website'
        db.create_table('shop_website', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Plan'])),
            ('domain', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('country', self.gf('django.db.models.fields.CharField')(default='', max_length=2)),
            ('currency', self.gf('django.db.models.fields.CharField')(default='EUR', max_length=3)),
            ('created', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('date_mod', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
        ))
        db.send_create_signal('shop', ['Website'])

        # Adding model 'Subscriptions'
        db.create_table('shop_subscriptions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_start', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_end', self.gf('django.db.models.fields.DateTimeField')()),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Plan'])),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Website'])),
        ))
        db.send_create_signal('shop', ['Subscriptions'])


    def backwards(self, orm):
        # Deleting model 'Carousel'
        db.delete_table('shop_carousel')

        # Deleting model 'Plan'
        db.delete_table('shop_plan')

        # Deleting model 'Feature'
        db.delete_table('shop_feature')

        # Deleting model 'FeaturePlugin'
        db.delete_table('cmsplugin_featureplugin')

        # Deleting model 'Website'
        db.delete_table('shop_website')

        # Deleting model 'Subscriptions'
        db.delete_table('shop_subscriptions')


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
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 18, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shop.carousel': {
            'Meta': {'object_name': 'Carousel'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'description_de': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'name_de': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'shop.feature': {
            'Meta': {'object_name': 'Feature'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'description_de': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'description_ru': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'html_class': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'name_de': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'shop.featureplugin': {
            'Meta': {'object_name': 'FeaturePlugin', 'db_table': "'cmsplugin_featureplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'feature1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins1'", 'to': "orm['shop.Feature']"}),
            'feature2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins2'", 'to': "orm['shop.Feature']"}),
            'feature3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins3'", 'to': "orm['shop.Feature']"})
        },
        'shop.plan': {
            'Meta': {'object_name': 'Plan'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'description_de': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'options': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'options_de': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'options_ru': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()', 'blank': 'True'})
        },
        'shop.subscriptions': {
            'Meta': {'object_name': 'Subscriptions'},
            'date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Plan']"}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Website']"})
        },
        'shop.website': {
            'Meta': {'object_name': 'Website'},
            'country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2'}),
            'created': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'EUR'", 'max_length': '3'}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Plan']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['shop']