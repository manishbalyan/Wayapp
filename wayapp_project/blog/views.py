from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from blog.models import Post
from django.shortcuts import get_object_or_404, render_to_response, redirect
from blog.forms import PostForm, UserForm, LoginForm


# helper function
def encode_url(url):
	return url.replace(' ', '_')
# Create your views here.
def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	popular_posts = Post.objects.order_by('-views')[:5]
	t = loader.get_template('blog/index.html')
	context_dict = {'latest_posts': latest_posts, 'popular_posts': popular_posts,}
	for post in latest_posts:
		post.url = encode_url(post.title)
	for popular_post in popular_posts:
		popular_post.url = encode_url(popular_post.title)	
	c = Context(context_dict)	
	return HttpResponse(t.render(c))

def post(request, post_url):
	single_post = get_object_or_404(Post, title = post_url.replace('_', ' '))
	popular_posts = Post.objects.order_by('-views')[:5]
	single_post.views += 1  # increment the no of views
	single_post.save() #save it
	t = loader.get_template('blog/post.html')
	c = Context({'single_post': single_post, 'popular_posts': popular_posts,})
	return HttpResponse(t.render(c))

def add_post(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid(): # is the form valid
			form.save(commit=True) # yes and save to db
			return redirect(index)
		else:
			print form.errors  # no, display error to end user
	else:
		form = PostForm()
	return render_to_response('blog/add_post.html', {'form': form}, context)	

def register(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)
		if form.is_valid(): # is the form valid
			form.save(commit=True) # yes and save to db
			return redirect(index)
		else:
			print form.errors  # no, display error to end user
	else:
		form = UserForm()
	return render_to_response('blog/register.html', {'form': form}, context)

def login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = LoginForm(request.POST, request.FILES)
		if form.is_valid(): # is the form valid
			form.save(commit=True) # yes and save to db
			return redirect(index)
		else:
			print form.errors  # no, display error to end user
	else:
		form = LoginForm()
	return render_to_response('blog/login.html', {'form': form}, context)
		
