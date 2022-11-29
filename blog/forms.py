from .models import Comment, Blog
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    """
    comments form
    """
    class Meta:
        model = Comment
        fields = ('body',)
