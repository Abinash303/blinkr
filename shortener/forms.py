from django import forms
from .models import URL

class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your long URL'})
        }
