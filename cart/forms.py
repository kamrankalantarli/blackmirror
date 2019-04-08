from django import forms
from .models import Comment


class CommentaForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'sname',
            'email',
            'g',
            's',
            'd',

        ]

