from django.http import HttpResponse
from django.template import loader
from blog.models import Post

def index(request):
    latest_posts = Post.objects.all()[:10]
    template = loader.get_template('main/index.html')
    context = {
            'latest_posts' : latest_posts
    }
    return HttpResponse(template.render(context, request))

