# Code I wrote
from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'description', 'file']
# End of Code I wrote