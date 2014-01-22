from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render, get_object_or_404

from blog.models import Post
from taggit.models import Tag

class IndexView(generic.ListView):
    context_object_name = 'latest'
    template_name = "blog/main/index.html"
    paginate_by = '10'
    queryset = Post.objects.all().order_by('-date')


class TaggedIndexView(generic.ListView):
    template_name = "blog/main/index.html"
    context_object_name = 'latest'
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug')).order_by('-date')

class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/main/detail.html" 
        
class PageIndexView(generic.ListView):
    context_object_name = 'latest'
    def get_context_data(self, **kwargs):
        context = super(PageIndexView, self).get_context_data(**kwargs)
        context["page"] = self.kwargs.get('slug')
        return context
    def get_template_names(self):
        return 'blog/pages/' + self.kwargs.get('slug') + '.html'
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug')).order_by('-date')
    
class PageDetail(generic.DetailView):
    model = Post
    def get_template_names(self):
        return 'blog/pages/' + self.kwargs.get('slug') + '_detail.html'

class Test(generic.DetailView):
    model = Post
    def get_template_names(self):
        return 'blog/main/' + self.kwargs.get('slug') + '.html'
    def get_context_data(self, **kwargs):
        context = super(Test, self).get_context_data(**kwargs)
        context['testcontext'] = "probando"
        return context
