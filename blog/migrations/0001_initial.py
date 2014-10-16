# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('author_email', models.EmailField(null=True, max_length=75)),
                ('date_creation', models.DateTimeField(null=True)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', models.CharField(null=True, max_length=140)),
                ('author', models.CharField(null=True, max_length=30)),
                ('author_email', models.EmailField(null=True, max_length=75)),
                ('date_creation', models.DateTimeField()),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='record',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='record',
            name='thread',
            field=models.ForeignKey(to='blog.Thread'),
            preserve_default=True,
        ),
    ]
