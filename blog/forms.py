from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    comments form
    """
    class Meta:
        model = Comment
        fields = ('body',)
