from django.contrib import admin
from pytils.translit import slugify

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    filter = ['created_at']

    def save_model(self, request, obj, form, change):
        if "title" in form.changed_data and "slug" not in form.changed_data:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)