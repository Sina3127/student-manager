from ckeditor.fields import RichTextField
from django.db import models


class Contract(models.Model):
    content = RichTextField(config_name='default')
    last_update = models.DateTimeField(auto_now=True)
