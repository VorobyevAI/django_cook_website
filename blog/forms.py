from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['create_at', 'post']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Почта'}),
            'website': forms.TextInput(attrs={'placeholder': 'Сайт'}),
            'message': forms.Textarea(attrs={'placeholder': 'Сообщение'})
        }
