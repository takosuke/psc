from django.contrib import admin
from blog.models import Post
    

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    fields =  ('title', 'date', 'text', 'url', 'tags', 'image')

admin.site.register(Post, PostAdmin)
