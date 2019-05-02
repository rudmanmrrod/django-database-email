from django.db import models

class EmailTemplate(models.Model):
  name = models.CharField(max_length=120,unique=True)
  mail = models.TextField()
