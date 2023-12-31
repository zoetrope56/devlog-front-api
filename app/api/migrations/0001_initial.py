# Generated by Django 4.1.13 on 2023-11-04 02:50

from django.db import migrations, models
import django.db.models.deletion
import django_tuieditor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('inp_dttm', models.DateTimeField(auto_now=True, db_column='INP_DTTM')),
                ('upd_dttm', models.DateTimeField(auto_now_add=True, db_column='UPD_DTTM')),
                ('ctnt_no', models.AutoField(db_column='CTNT_NO', primary_key=True, serialize=False)),
                ('ctnt_title', models.CharField(blank=True, db_column='CTNT_TITLE', max_length=100, null=True)),
                ('ctnt_subtitle', models.CharField(blank=True, db_column='CTNT_SUBTITLE', max_length=150, null=True)),
                ('inp_user', models.CharField(blank=True, db_column='INP_USER', max_length=30, null=True)),
            ],
            options={
                'db_table': 'contents_mst',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('inp_dttm', models.DateTimeField(auto_now=True, db_column='INP_DTTM')),
                ('upd_dttm', models.DateTimeField(auto_now_add=True, db_column='UPD_DTTM')),
                ('file_no', models.AutoField(db_column='FILE_NO', primary_key=True, serialize=False)),
                ('file_path', models.CharField(blank=True, db_column='FILE_PATH', max_length=200, null=True)),
                ('file_name', models.CharField(blank=True, db_column='FILE_NAME', max_length=200, null=True)),
                ('file_ext', models.CharField(blank=True, db_column='FILE_EXT', max_length=200, null=True)),
                ('ctnt_no', models.IntegerField(blank=True, db_column='CTNT_NO', null=True)),
            ],
            options={
                'db_table': 'file_mst',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('inp_dttm', models.DateTimeField(auto_now=True, db_column='INP_DTTM')),
                ('upd_dttm', models.DateTimeField(auto_now_add=True, db_column='UPD_DTTM')),
                ('tag_no', models.AutoField(db_column='TAG_NO', primary_key=True, serialize=False)),
                ('tag_name', models.CharField(blank=True, db_column='TAG_NAME', max_length=15, null=True)),
            ],
            options={
                'db_table': 'tags_mst',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('inp_dttm', models.DateTimeField(auto_now=True, db_column='INP_DTTM')),
                ('upd_dttm', models.DateTimeField(auto_now_add=True, db_column='UPD_DTTM')),
                ('user_no', models.AutoField(db_column='USER_NO', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='USERNAME', max_length=30, null=True)),
                ('password', models.CharField(blank=True, db_column='PASSWORD', max_length=100, null=True)),
                ('grant', models.CharField(blank=True, db_column='GRANT', max_length=10, null=True)),
            ],
            options={
                'db_table': 'user_mst',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContentsDetail',
            fields=[
                ('ctnt_dtl_no', models.OneToOneField(db_column='CTNT_NO', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ctnt_dtl_n', serialize=False, to='api.content')),
                ('ctnt_dtl_title', models.CharField(blank=True, db_column='CTNT_TITLE', max_length=100, null=True)),
                ('ctnt_dtl_inp_user', models.CharField(blank=True, db_column='INP_USER', max_length=30, null=True)),
                ('ctnt_body', django_tuieditor.models.MarkdownField(blank=True, null=True)),
                ('ctnt_path', models.CharField(blank=True, db_column='CTNT_PATH', max_length=200, null=True)),
                ('ctnt_name', models.CharField(blank=True, db_column='CTNT_NAME', max_length=200, null=True)),
                ('ctnt_ext', models.CharField(blank=True, db_column='CTNT_EXT', max_length=200, null=True)),
            ],
            options={
                'db_table': 'contents_dtl',
                'managed': False,
            },
            bases=('api.content',),
        ),
        migrations.CreateModel(
            name='ContentsTag',
            fields=[
                ('content_tag_no', models.OneToOneField(db_column='TAG_NO', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.tag')),
                ('ctnt_no', models.IntegerField(blank=True, db_column='CTNT_NO', null=True)),
                ('sort', models.IntegerField(blank=True, db_column='SORT', null=True)),
            ],
            options={
                'db_table': 'contents_tags',
                'managed': False,
            },
            bases=('api.tag',),
        ),
    ]
