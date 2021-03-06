# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-12 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TalkUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SlackAuth',
            fields=[
                ('auth_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='converse.Auth')),
                ('access_token', models.CharField(max_length=200)),
                ('team_id', models.CharField(max_length=30, unique=True)),
                ('team_name', models.CharField(max_length=200)),
                ('bot_id', models.CharField(max_length=30)),
                ('bot_access_token', models.CharField(max_length=200)),
            ],
            bases=('converse.auth',),
        ),
        migrations.CreateModel(
            name='SlackChannel',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='converse.Group')),
                ('slack_id', models.CharField(max_length=30)),
                ('is_main', models.BooleanField(default=False)),
                ('slack_auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slack_channels', to='converse.SlackAuth')),
            ],
            bases=('converse.group',),
        ),
        migrations.CreateModel(
            name='SlackUser',
            fields=[
                ('talkuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='converse.TalkUser')),
                ('slack_id', models.CharField(max_length=30)),
                ('slack_auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slack_users', to='converse.SlackAuth')),
            ],
            bases=('converse.talkuser',),
        ),
        migrations.AlterUniqueTogether(
            name='slackuser',
            unique_together=set([('slack_id', 'slack_auth')]),
        ),
        migrations.AlterUniqueTogether(
            name='slackchannel',
            unique_together=set([('slack_id', 'slack_auth')]),
        ),
    ]
