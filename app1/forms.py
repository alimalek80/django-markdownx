from django import forms
from .models import MarkdownExample

class MarkDownExampleForm(forms.ModelForm):
    class Meta:

        model = MarkdownExample
        fields = '__all__'