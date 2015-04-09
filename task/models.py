from django.db import models

class Task(models.Model):
	completed= models.BooleanField(default=False)
	title= models.CharField(max_length=128)
	description= models.TextField()


	def __unicode__(self):
		return self.title
		
