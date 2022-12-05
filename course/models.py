from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
	username = models.CharField(max_length=50)
	text = models.TextField()
	date = models.DateTimeField(default=timezone.now, blank=True)