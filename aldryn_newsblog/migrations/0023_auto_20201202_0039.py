# Generated by Django 2.2.9 on 2020-12-01 23:39

import aldryn_apphooks_config.fields
import aldryn_newsblog.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djangocms_text_ckeditor.fields
import filer.fields.image
import sortedm2m.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0022_delete_old_categories_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='category',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='category',
            name='rgt',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tree_id',
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, to='aldryn_newsblog.Category', verbose_name='Kategorien'),
        ),
    ]
