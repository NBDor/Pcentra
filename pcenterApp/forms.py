from django import forms
from .models import Url

class UrlForm(forms.ModelForm):
    
    full_link = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Enter URL link"}))

    class Meta:
        model = Url

        fields = ('full_link',)