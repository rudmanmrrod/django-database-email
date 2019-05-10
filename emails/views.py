from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import *
from .models import *

class MailListView(ListView):
  model = EmailTemplate
  template_name = "email.list.html"
  paginate_by = 10

class MailCreateView(CreateView):
  form_class = EmailForm
  model = EmailTemplate
  template_name = "email.create.html"
  success_url = reverse_lazy("emails:list_email")

class GetFieldsView(View):

  def get(self, request, **kwargs):
    try:
      pk = request.GET.get('pk')
      content_type = ContentType.objects.get(pk=int(pk))
      current_model = apps.get_model(content_type.app_label,content_type.model)
      fields = [f.name for f in current_model._meta.get_fields()]
      return JsonResponse({'fields':fields}, safe=False)
    except Exception as e:
      print(e)
      return JsonResponse([], safe=False)

class MailPreview(DetailView):
  model = EmailTemplate
  template_name = "email.preview.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    mail = self.object
    data = {'username':'Rudman'}
    context['preview'] = mail.validate_email_content(**data)
    return context