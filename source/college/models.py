from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class Contract(models.Model):
    title = models.CharField(max_length=256)
    content = RichTextField(config_name='default')
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Agreement(models.Model):
    students_name = models.CharField(max_length=30)
    number_of_classes = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Duration(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()  # todo end_date >>> start_date
    agreement = models.ForeignKey(Agreement, on_delete=models.PROTECT)
