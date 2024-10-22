
from django.db import models
from django.utils import timezone

# Create your models here.
class blogcontent(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(default="")
    date_added = models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.title