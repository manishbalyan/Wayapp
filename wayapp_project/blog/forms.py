from django import forms
from blog.models import Post

# we create ModelForm class which mapped to our model via the meta class 
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'tag', 'image']