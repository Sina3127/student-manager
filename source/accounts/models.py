from django.contrib.auth.models import User
from django.core.validators import validate_image_file_extension
from django.db import models


class Signatures(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, validators=[validate_image_file_extension, ])
    img = models.ImageField(upload_to='uploads/')
    last_update = models.DateTimeField(auto_now=True)
