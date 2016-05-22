# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('notes', models.TextField()),
                ('proj_credits', models.TextField()),
                ('state', models.CharField(max_length=1)),
                ('admin_notes', models.TextField()),
                ('sharp_file', models.FileField(upload_to='projects')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(to='sharpsite.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('rtype', models.CharField(max_length=2)),
                ('project', models.ForeignKey(to='sharpsite.Project', null=True, blank=True)),
                ('project_comment', models.ForeignKey(to='sharpsite.ProjectComment', null=True, blank=True)),
                ('reported', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reported')),
                ('reporter', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reporter')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('notes', models.TextField()),
                ('admin_notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamComment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(to='sharpsite.Team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamRank',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('team', models.ForeignKey(to='sharpsite.Team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamRankPermission',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('delete_comments', models.BooleanField()),
                ('add_comments', models.BooleanField()),
                ('rm_member', models.BooleanField()),
                ('demote_lower_member', models.BooleanField()),
                ('demote_equal_member', models.BooleanField()),
                ('demote_higher_member', models.BooleanField()),
                ('promote_to_equal', models.BooleanField()),
                ('promote_to_higher', models.BooleanField()),
                ('invite_member', models.BooleanField()),
                ('block_member', models.BooleanField()),
                ('edit_ranks', models.BooleanField()),
                ('delete_team', models.BooleanField()),
                ('edit_notes', models.BooleanField()),
                ('rank', models.ForeignKey(to='sharpsite.TeamRank')),
            ],
        ),
        migrations.CreateModel(
            name='UserAlert',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('dismissed', models.BooleanField()),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='from+')),
                ('to', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='commented_on')),
            ],
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('to', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('about_me', models.TextField()),
                ('ban_alert', models.ForeignKey(to='sharpsite.UserAlert', null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='teammembers',
            name='rank',
            field=models.ForeignKey(to='sharpsite.TeamRank'),
        ),
        migrations.AddField(
            model_name='teammembers',
            name='team',
            field=models.ForeignKey(to='sharpsite.Team'),
        ),
        migrations.AddField(
            model_name='report',
            name='team',
            field=models.ForeignKey(to='sharpsite.Team', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='report',
            name='team_comment',
            field=models.ForeignKey(to='sharpsite.TeamComment', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='report',
            name='user_comment',
            field=models.ForeignKey(to='sharpsite.UserComment', null=True, blank=True),
        ),
    ]
