import re
from django.db import models
from django.template import Context, Template

class EmailTemplate(models.Model):
  name = models.CharField(max_length=120,unique=True)
  mail = models.TextField()

  class Meta:
    ordering = ('pk',)

  def validate_email_content(self,**args):
    expresions = re.findall(r"\{\{(.*?)\}\}", self.mail)
    for item in args.keys():
      if item not in expresions:
        return False
    template = Template(self.mail)
    context = Context(args)
    return template.render(context)