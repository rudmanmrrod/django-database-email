from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import *

class EmailForm(forms.ModelForm):

  models = forms.ChoiceField(choices=ContentType.objects.values_list('id','model'),
    widget=forms.Select(attrs={'onchange':'loadFields(this.value)'}),
    required=False)

  fields = forms.ChoiceField(choices=(('',''),),required=False)

  class Meta:
    model = EmailTemplate
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['mail'].widget.attrs.update({'class': 'trumbowyg'})