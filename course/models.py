from django.db import models
from datetime import datetime

# Create your models here.
class Comment(models.Model):
	username = models.CharField(max_length=50)
	text = models.TextField()
	date = models.DateTimeField(default=datetime.now, blank=True)