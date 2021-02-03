# Generated by Django 2.2.17 on 2021-02-03 18:05

import aldryn_apphooks_config.fields
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
        ('aldryn_newsblog', '0023_auto_20201202_0039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsblogconfig',
            options={'permissions': (('can_edit_section_placeholder', 'Can edit Section placeholders'),), 'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
    ]
