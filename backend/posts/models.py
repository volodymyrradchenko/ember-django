from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=100, blank=True, default='')
	body = models.TextField(default='')
	url = models.URLField(default='')

	class Meta:
		ordering = ('id',)