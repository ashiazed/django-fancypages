# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ('assets', '0001_initial'),
    )

    def forwards(self, orm):
        # Adding model 'PageType'
        db.create_table(u'fancypages_pagetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=128)),
            ('template_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('fancypages', ['PageType'])

        # Adding model 'VisibilityType'
        db.create_table(u'fancypages_visibilitytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal('fancypages', ['VisibilityType'])

        # Adding model 'FancyPage'
        db.create_table(u'fancypages_fancypage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('depth', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('numchild', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('page_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pages', null=True, to=orm['fancypages.PageType'])),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default=u'draft', max_length=15)),
            ('date_visible_start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_visible_end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('fancypages', ['FancyPage'])

        # Adding M2M table for field visibility_types on 'FancyPage'
        m2m_table_name = db.shorten_name(u'fancypages_fancypage_visibility_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fancypage', models.ForeignKey(orm['fancypages.fancypage'], null=False)),
            ('visibilitytype', models.ForeignKey(orm['fancypages.visibilitytype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['fancypage_id', 'visibilitytype_id'])

        # Adding model 'Container'
        db.create_table(u'fancypages_container', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
        ))
        db.send_create_signal('fancypages', ['Container'])

        # Adding model 'OrderedContainer'
        db.create_table(u'fancypages_orderedcontainer', (
            (u'container_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.Container'], unique=True, primary_key=True)),
            ('display_order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('fancypages', ['OrderedContainer'])

        # Adding model 'ContentBlock'
        db.create_table(u'fancypages_contentblock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blocks', to=orm['fancypages.Container'])),
            ('display_order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('fancypages', ['ContentBlock'])

        # Adding model 'TextBlock'
        db.create_table(u'fancypages_textblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(default='Your text goes here.')),
        ))
        db.send_create_signal('fancypages', ['TextBlock'])

        # Adding model 'TitleTextBlock'
        db.create_table(u'fancypages_titletextblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Your title goes here.', max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')(default='Your text goes here.')),
        ))
        db.send_create_signal('fancypages', ['TitleTextBlock'])

        # Adding model 'ImageBlock'
        db.create_table(u'fancypages_imageblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('alt_text', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('image_asset', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='image_blocks', null=True, to=orm['assets.ImageAsset'])),
        ))
        db.send_create_signal('fancypages', ['ImageBlock'])

        # Adding model 'ImageAndTextBlock'
        db.create_table(u'fancypages_imageandtextblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('alt_text', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('image_asset', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='image_text_blocks', null=True, to=orm['assets.ImageAsset'])),
            ('text', self.gf('django.db.models.fields.CharField')(default='Your text goes here.', max_length=2000)),
        ))
        db.send_create_signal('fancypages', ['ImageAndTextBlock'])

        # Adding model 'CarouselBlock'
        db.create_table(u'fancypages_carouselblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
            ('image_1', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='+', null=True, to=orm['assets.ImageAsset'])),
            ('link_url_1', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('image_2', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='+', null=True, to=orm['assets.ImageAsset'])),
            ('link_url_2', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('image_3', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='+', null=True, to=orm['assets.ImageAsset'])),
            ('link_url_3', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('image_4', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='+', null=True, to=orm['assets.ImageAsset'])),
            ('link_url_4', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('image_5', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='+', null=True, to=orm['assets.ImageAsset'])),
            ('link_url_5', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('image_6', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='+', null=True, to=orm['assets.ImageAsset'])),
            ('link_url_6', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('image_7', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='+', null=True, to=orm['assets.ImageAsset'])),
            ('link_url_7', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('image_8', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='+', null=True, to=orm['assets.ImageAsset'])),
            ('link_url_8', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('image_9', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='+', null=True, to=orm['assets.ImageAsset'])),
            ('link_url_9', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('image_10', self.gf('fancypages.assets.fields.AssetKey')(blank=True, related_name='+', null=True, to=orm['assets.ImageAsset'])),
            ('link_url_10', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal('fancypages', ['CarouselBlock'])

        # Adding model 'PageNavigationBlock'
        db.create_table(u'fancypages_pagenavigationblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fancypages', ['PageNavigationBlock'])

        # Adding model 'PrimaryNavigationBlock'
        db.create_table(u'fancypages_primarynavigationblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fancypages', ['PrimaryNavigationBlock'])

        # Adding model 'TabBlock'
        db.create_table(u'fancypages_tabblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fancypages', ['TabBlock'])

        # Adding model 'TwoColumnLayoutBlock'
        db.create_table(u'fancypages_twocolumnlayoutblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
            ('left_width', self.gf('django.db.models.fields.PositiveIntegerField')(default=6, max_length=3)),
        ))
        db.send_create_signal('fancypages', ['TwoColumnLayoutBlock'])

        # Adding model 'ThreeColumnLayoutBlock'
        db.create_table(u'fancypages_threecolumnlayoutblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fancypages', ['ThreeColumnLayoutBlock'])

        # Adding model 'FourColumnLayoutBlock'
        db.create_table(u'fancypages_fourcolumnlayoutblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fancypages', ['FourColumnLayoutBlock'])

        # Adding model 'VideoBlock'
        db.create_table(u'fancypages_videoblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('video_code', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('fancypages', ['VideoBlock'])

        # Adding model 'TwitterBlock'
        db.create_table(u'fancypages_twitterblock', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fancypages.ContentBlock'], unique=True, primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('max_tweets', self.gf('django.db.models.fields.PositiveIntegerField')(default=5)),
        ))
        db.send_create_signal('fancypages', ['TwitterBlock'])


    def backwards(self, orm):
        # Deleting model 'PageType'
        db.delete_table(u'fancypages_pagetype')

        # Deleting model 'VisibilityType'
        db.delete_table(u'fancypages_visibilitytype')

        # Deleting model 'FancyPage'
        db.delete_table(u'fancypages_fancypage')

        # Removing M2M table for field visibility_types on 'FancyPage'
        db.delete_table(db.shorten_name(u'fancypages_fancypage_visibility_types'))

        # Deleting model 'Container'
        db.delete_table(u'fancypages_container')

        # Deleting model 'OrderedContainer'
        db.delete_table(u'fancypages_orderedcontainer')

        # Deleting model 'ContentBlock'
        db.delete_table(u'fancypages_contentblock')

        # Deleting model 'TextBlock'
        db.delete_table(u'fancypages_textblock')

        # Deleting model 'TitleTextBlock'
        db.delete_table(u'fancypages_titletextblock')

        # Deleting model 'ImageBlock'
        db.delete_table(u'fancypages_imageblock')

        # Deleting model 'ImageAndTextBlock'
        db.delete_table(u'fancypages_imageandtextblock')

        # Deleting model 'CarouselBlock'
        db.delete_table(u'fancypages_carouselblock')

        # Deleting model 'PageNavigationBlock'
        db.delete_table(u'fancypages_pagenavigationblock')

        # Deleting model 'PrimaryNavigationBlock'
        db.delete_table(u'fancypages_primarynavigationblock')

        # Deleting model 'TabBlock'
        db.delete_table(u'fancypages_tabblock')

        # Deleting model 'TwoColumnLayoutBlock'
        db.delete_table(u'fancypages_twocolumnlayoutblock')

        # Deleting model 'ThreeColumnLayoutBlock'
        db.delete_table(u'fancypages_threecolumnlayoutblock')

        # Deleting model 'FourColumnLayoutBlock'
        db.delete_table(u'fancypages_fourcolumnlayoutblock')

        # Deleting model 'VideoBlock'
        db.delete_table(u'fancypages_videoblock')

        # Deleting model 'TwitterBlock'
        db.delete_table(u'fancypages_twitterblock')


    models = {
        u'assets.imageasset': {
            'Meta': {'object_name': 'ImageAsset'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'height': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fancypages.carouselblock': {
            'Meta': {'ordering': "['display_order']", 'object_name': 'CarouselBlock', '_ormbases': ['fancypages.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'image_1': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'image_10': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'image_2': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'image_3': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'image_4': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'image_5': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'image_6': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'image_7': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'image_8': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'image_9': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'link_url_1': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'link_url_10': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'link_url_2': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'link_url_3': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'link_url_4': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'link_url_5': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'link_url_6': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'link_url_7': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'link_url_8': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'link_url_9': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'fancypages.container': {
            'Meta': {'object_name': 'Container'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'fancypages.contentblock': {
            'Meta': {'ordering': "['display_order']", 'object_name': 'ContentBlock'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blocks'", 'to': "orm['fancypages.Container']"}),
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'fancypages.fancypage': {
            'Meta': {'object_name': 'FancyPage'},
            'date_visible_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_visible_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'page_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pages'", 'null': 'True', 'to': "orm['fancypages.PageType']"}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "u'draft'", 'max_length': '15'}),
            'visibility_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fancypages.VisibilityType']", 'symmetrical': 'False'})
        },
        'fancypages.fourcolumnlayoutblock': {
            'Meta': {'object_name': 'FourColumnLayoutBlock'},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'fancypages.imageandtextblock': {
            'Meta': {'object_name': 'ImageAndTextBlock', '_ormbases': ['fancypages.ContentBlock']},
            'alt_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'image_asset': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'image_text_blocks'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'default': "'Your text goes here.'", 'max_length': '2000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'fancypages.imageblock': {
            'Meta': {'object_name': 'ImageBlock', '_ormbases': ['fancypages.ContentBlock']},
            'alt_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'image_asset': ('fancypages.assets.fields.AssetKey', [], {'blank': 'True', 'related_name': "'image_blocks'", 'null': 'True', 'to': u"orm['assets.ImageAsset']"}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'fancypages.orderedcontainer': {
            'Meta': {'object_name': 'OrderedContainer', '_ormbases': ['fancypages.Container']},
            u'container_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.Container']", 'unique': 'True', 'primary_key': 'True'}),
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'fancypages.pagenavigationblock': {
            'Meta': {'ordering': "['display_order']", 'object_name': 'PageNavigationBlock', '_ormbases': ['fancypages.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'fancypages.pagetype': {
            'Meta': {'object_name': 'PageType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'fancypages.primarynavigationblock': {
            'Meta': {'ordering': "['display_order']", 'object_name': 'PrimaryNavigationBlock', '_ormbases': ['fancypages.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'fancypages.tabblock': {
            'Meta': {'ordering': "['display_order']", 'object_name': 'TabBlock', '_ormbases': ['fancypages.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'fancypages.textblock': {
            'Meta': {'ordering': "['display_order']", 'object_name': 'TextBlock', '_ormbases': ['fancypages.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "'Your text goes here.'"})
        },
        'fancypages.threecolumnlayoutblock': {
            'Meta': {'object_name': 'ThreeColumnLayoutBlock'},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'fancypages.titletextblock': {
            'Meta': {'ordering': "['display_order']", 'object_name': 'TitleTextBlock', '_ormbases': ['fancypages.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "'Your text goes here.'"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Your title goes here.'", 'max_length': '100'})
        },
        'fancypages.twitterblock': {
            'Meta': {'ordering': "['display_order']", 'object_name': 'TwitterBlock', '_ormbases': ['fancypages.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'max_tweets': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'fancypages.twocolumnlayoutblock': {
            'Meta': {'object_name': 'TwoColumnLayoutBlock'},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'left_width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '6', 'max_length': '3'})
        },
        'fancypages.videoblock': {
            'Meta': {'ordering': "['display_order']", 'object_name': 'VideoBlock', '_ormbases': ['fancypages.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fancypages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'video_code': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'fancypages.visibilitytype': {
            'Meta': {'object_name': 'VisibilityType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fancypages']
