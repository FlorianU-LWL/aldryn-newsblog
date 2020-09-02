# Generated by Django 2.2.9 on 2020-08-11 23:04

import aldryn_newsblog.fields
import aldryn_newsblog.fields
import aldryn_translation_tools.models
import django.db.models.deletion
import parler.fields
import parler.models
from aldryn_categories.models import Category as OldCategory
from aldryn_newsblog.models import Article
from aldryn_newsblog.models import Category as NewCategory
from aldryn_newsblog.cms_appconfig import NewsBlogConfig
from django.conf import settings
from django.db import migrations
from django.db import models
from django.utils import translation

translation.activate(settings.LANGUAGE_CODE)


def dump_categories_data(apps, schema_editor, **context) -> dict:
    for category in OldCategory.get_root_nodes():
        if _is_wrong_blog_related_to_categories_tree(category):
            raise Exception(
                f'One or several of descendants of this category are linked to articles from different blogs: {category.safe_translation_getter("name", language_code=settings.LANGUAGE_CODE, any_language=True)}')

    categories_data_list = prepare_category_data_list(OldCategory.get_root_nodes())
    upload_categories_data(categories_data_list)
    assign_blog_configs()


def _is_wrong_blog_related_to_categories_tree(root_category: OldCategory) -> bool:
    tree_related_app_configs = list([article.app_config for article in root_category.article_set.all()])
    for category in root_category.get_descendants():
        tree_related_app_configs.extend([article.app_config for article in category.article_set.all()])
    count_of_related_blogs = len(set(tree_related_app_configs))
    return count_of_related_blogs > 1


def prepare_category_data_list(categories) -> list:
    data_list = list()
    for category in categories:
        category_data = dict(
            name=category.safe_translation_getter('name', language_code=settings.LANGUAGE_CODE, any_language=True),
            slug=category.safe_translation_getter('slug', language_code=settings.LANGUAGE_CODE, any_language=True),
            lft=category.lft,
            rgt=category.rgt,
            tree_id=category.tree_id,
            depth=category.depth,
            related_articles=[article.pk for article in category.article_set.all()],
        )
        if category.get_children():
            category_data['children'] = prepare_category_data_list(category.get_children())

        data_list.append(category_data)
    return data_list


def upload_categories_data(categories_data_list: list):
    for data in categories_data_list:
        new_category = NewCategory.objects.create(
            name=data.get('name'),
            slug=data.get('slug'),
            lft=data.get('lft'),
            rgt=data.get('rgt'),
            tree_id=data.get('tree_id'),
            depth=data.get('depth'),
            newsblog_config=NewsBlogConfig.objects.first()
        )
        for article_pk in data.get('related_articles'):
            article = Article.objects.get(pk=article_pk)
            article.new_categories.add(new_category)
            article.save()

        if data.get('children'):
            upload_categories_data(data.get('children'))


def assign_blog_configs():
    for root_category in OldCategory.get_root_nodes():
        tree_related_app_configs = list([article.app_config for article in root_category.article_set.all()])
        for category in root_category.get_descendants():
            tree_related_app_configs.extend([article.app_config for article in category.article_set.all()])

        if tree_related_app_configs:
            newsblog_config = list(set(tree_related_app_configs))[0]
        else:
            newsblog_config = None

        new_category = NewCategory.objects.get(translations__slug=root_category.slug)
        if newsblog_config:
            new_category.newsblog_config = newsblog_config
        new_category.save()
        for category in root_category.get_descendants():
            new_category = NewCategory.objects.get(translations__slug=category.slug)
            if newsblog_config:
                new_category.newsblog_config = newsblog_config
            new_category.save()


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0019_auto_20200812_0104'),
    ]

    operations = [
        migrations.RunPython(dump_categories_data),

        # migrations.RemoveField(
        #     model_name='article',
        #     name='categories',
        # ),
        # migrations.RenameField(
        #     model_name='article',
        #     old_name='new_categories',
        #     new_name='categories',
        # ),
    ]