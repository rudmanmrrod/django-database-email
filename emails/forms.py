from django import forms
from .models import *

class EmailForm(forms.ModelForm):
  class Meta:
    model = EmailTemplate
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['mail'].widget.attrs.update({'class': 'trumbowyg'})