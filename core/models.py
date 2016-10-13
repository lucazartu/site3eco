from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

from django.db import models

class Post(models.Model):
	"""Model for a post"""
	title = models.CharField(max_length=250)
	date = models.DateTimeField()
	text = models.TextField()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __unicode__(self):
		return self.title
