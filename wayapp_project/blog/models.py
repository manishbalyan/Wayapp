from django.db import models
from uuslug import uuslug
# Create your models here.
# using django orm mapping function
# post class defines db gtable representing a single post
# Django ORM provides a database abstraction layer used for interacting with db using CRUD via python objets
class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length = 100)
	content = models.TextField()
	tag = models.CharField(max_length = 20, blank = True, null = True) # setting blank true we indicate that field is not required and can be left blank null true allow blank values to be stored in db as Null.
	image = models.ImageField(upload_to = "images", blank = True, null = True)
	views = models.IntegerField(default = 0)
	slug = models.CharField(max_length=100, unique = True)
	def __unicode__(self):
		return self.title
	def save(self, *args, **kwargs):
		self.slug = uuslug(self.title, instance = self, max_length = 100)
		super(Post, self).save(*args, **kwargs)
			