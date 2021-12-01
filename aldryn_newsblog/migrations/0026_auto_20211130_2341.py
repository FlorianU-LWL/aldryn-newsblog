# Generated by Django 2.2.24 on 2021-11-30 22:41

import aldryn_translation_tools.models
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0025_auto_20210421_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsblog_config', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aldryn_newsblog.NewsBlogConfig')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
            bases=(aldryn_translation_tools.models.TranslatedAutoSlugifyMixin, aldryn_translation_tools.models.TranslationHelperMixin, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='article',
            name='article_tags',
            field=models.ManyToManyField(blank=True, to='aldryn_newsblog.ArticleTag', verbose_name='tags'),
        ),
        migrations.CreateModel(
            name='ArticleTagTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(default='', max_length=255, verbose_name='name')),
                ('slug', models.SlugField(blank=True, default='', help_text='Provide a “slug” or leave blank for an automatically generated one.', max_length=255, verbose_name='slug')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='aldryn_newsblog.ArticleTag')),
            ],
            options={
                'verbose_name': 'tag Translation',
                'db_table': 'aldryn_newsblog_articletag_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master'), ('language_code', 'slug')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
