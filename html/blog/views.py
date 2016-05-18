from django.shortcuts import render
from django.views import generic

from blog.models import Post
#from taggit.models import Tag
# Create your views here.

class IndexView(generic.ListView):
    context_object_name = 'latest'
    template_name = "blog/main/index.html"
    paginate_by = '10'
    queryset = Post.objects.all().order_by('-date')
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
#        context['alltags'] = Tag.objects.annotate(num_tags=Count('post')).order_by('-num_tags')[:12]
        return context

class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/main/detail.html" 
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
#        context['alltags'] = Tag.objects.annotate(num_tags=Count('post')).order_by('-num_tags')[:12]
        return context
        
class PageIndexView(generic.ListView):
    context_object_name = 'latest'
    def get_context_data(self, **kwargs):
        context = super(PageIndexView, self).get_context_data(**kwargs)
        context["page"] = self.kwargs.get('slug')
#        context['alltags'] = Tag.objects.annotate(num_tags=Count('post')).order_by('-num_tags')[:12]
        return context
    def get_template_names(self):
        return 'blog/pages/' + self.kwargs.get('slug') + '.html'
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug')).order_by('-date')
    
class PageDetail(generic.DetailView):
    model = Post
    def get_template_names(self):
        return 'blog/pages/' + self.kwargs.get('slug') + '_detail.html'
    def get_context_data(self, **kwargs):
        context = super(PageDetail, self).get_context_data(**kwargs)
#        context['alltags'] = Tag.objects.annotate(num_tags=Count('post')).order_by('-num_tags')[:12]
        return context
