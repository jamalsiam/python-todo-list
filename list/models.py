from django.db import models
from django.utils import timezone

class Address(models.Model):
    name = models.CharField(max_length = 20)
    location = models.TextField()
    data_added = models.DateTimeField(default = timezone.now)

    def _str_(self) :
       return '<Name:{},ID:{}>'.format(self.name, self.id)