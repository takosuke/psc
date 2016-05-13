# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
                ('text', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'cover', blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='Options: psc ||| events ||| food ||| records ||| art ||| video ||| releases ||| nemesis ||| pizza ||| animation ||| gif ||| shocking film ||| music ||| mierda ||| fatrobocop ||| press ||| phil & monica ||| video report ||| concerts ||| tv ||| psctv ||| report ||| retrasados ||| poetry ||| festival ||| seydisfjord ||| live ||| ', verbose_name='Tags')),
            ],
        ),
    ]
