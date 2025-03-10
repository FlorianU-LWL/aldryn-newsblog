from django.contrib import admin
from parler.admin import TranslatableAdmin

from aldryn_newsblog.cms_appconfig import NewsBlogConfig
from aldryn_newsblog.models import Category


class CategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'newsblog_config')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'slug',
                'newsblog_config',
            )
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == "newsblog_config":
                kwargs["queryset"] = NewsBlogConfig.objects.filter(site=request.site)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(newsblog_config__site=request.site)


admin.site.register(Category, CategoryAdmin)
