from django import forms
from django.forms import fields,ModelForm
from .models import post,comments


class post_form(ModelForm):

    class Meta:
        model=post
        fields=["title","post_image","caption"]

class commentform(ModelForm):
    class Meta:
        model=comments
        fields=['com']
        


