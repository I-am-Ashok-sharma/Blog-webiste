from django.shortcuts import get_object_or_404 ,render
from blog.models import Post
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.




def Post_list(request):
    Post_list = Post.objects.all()
    return render(request,'blog/list.html',{'Post_list':Post_list})

#class PostListView(ListView):
    #paginate_by = 2
    #model = Post

#class PostListView(ListView):
   # queryset = Post.published.all()
    #context_object_name = 'Post'
    #paginate_by = 3
    #template_name = 'blog/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request,'blog/detail.html',{'post':post})
