from django.contrib import admin
from .models import Blog, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    """
    Backend administration for Blog
    """
    summernote_fields = ('content')


admin.site.register(Comment)
