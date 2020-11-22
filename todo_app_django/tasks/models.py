from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    ###### Create date created, date finished
  #  pub_date = models.DateTimeField('date published')
  #  finished_date = models.DateTimeField('date finished')

    def __str__(self):
        return self.title