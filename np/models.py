from django.db import models
from django.utils import timezone

class Article(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	section = models.CharField(max_length=200)
	introductory_text = models.TextField()
	text = models.TextField()
	url = models.URLField()
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title