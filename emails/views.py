from django.views.generic import ListView
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

