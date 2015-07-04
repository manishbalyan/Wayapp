from django.test import TestCase
from models import post

# Create your tests here.
class PostTests(TestCase):
	def test_str(self):
		my_title = post(title = 'this is a basic title for basic test case')
		self.assertEquals(str(my_title), 'this is a basic title for basic test case',)