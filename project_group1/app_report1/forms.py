from django import forms
from .models import Disease

class DiseaseForm(forms.ModelForm):
    # Override symptoms to accept list of strings from multiple inputs
    symptoms = forms.CharField(widget=forms.HiddenInput(), required=False)  # We'll handle it manually

    class Meta:
        model = Disease
        fields = ['name', 'brief_description', 'detailed_description', 'treatment', 'image_url']
