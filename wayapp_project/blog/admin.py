from django.contrib import admin
from blog.models import Post
# Register your models here.
# here we are telling django which model we want available to the admin


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'views', )



admin.site.register(Post, PostAdmin)