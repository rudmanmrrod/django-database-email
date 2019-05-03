from django.urls import path
from .views import *

app_name = 'emails'
urlpatterns = [
  path('',MailListView.as_view(),name='list_email'),
  path('create/',MailCreateView.as_view(),name='create_email'),
  path('get-fields/',GetFieldsView.as_view(),name='get_fields'),
]
