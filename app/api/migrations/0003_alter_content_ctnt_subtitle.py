# Generated by Django 4.1.13 on 2023-11-05 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_content_options_alter_contentsdetail_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='ctnt_subtitle',
            field=models.CharField(blank=True, db_column='CTNT_SUBTITLE', max_length=300, null=True),
        ),
    ]