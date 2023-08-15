from django import forms
from .models import Film, Comments


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'state', 'date_exist', 'desc', 'rate')
# поля pub_date и id заполняются сами


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
