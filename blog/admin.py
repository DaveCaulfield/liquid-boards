from django.contrib import admin
from .models import Blog, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    """
    Backend administration for Blog
    """
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('author', 'created_on')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    backend administration comment area
    """
    list_display = ('name', 'blog', 'body', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ['name', 'body']
