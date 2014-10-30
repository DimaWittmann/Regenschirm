# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('author_email', models.EmailField(max_length=75, null=True)),
                ('date_creation', models.DateTimeField(null=True)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('record', models.ForeignKey(to='blog.Record')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
