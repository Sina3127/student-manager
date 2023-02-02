from django.contrib.auth.models import User
from django.db import models


class Signatures(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    img = models.ImageField(upload_to='uploads/')
