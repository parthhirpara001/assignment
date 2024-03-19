from django import forms
from .models import *

class postorm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'