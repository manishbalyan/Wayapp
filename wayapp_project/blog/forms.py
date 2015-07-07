from django import forms
from blog.models import Post, User, Login


# we create ModelForm class which mapped to our model via the meta class 
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'tag', 'image']

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name', 'email', 'password']	

class LoginForm(forms.ModelForm):
	class Meta:
		model = Login
		fields = ['username', 'password']	