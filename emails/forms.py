from django import forms
from .models import *

class EmailForm(forms.ModelForm):
  class Meta:
    model = EmailTemplate
    fields = '__all__'