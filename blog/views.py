from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(estado=1).order_by('-creado')
    paginate_by = '5'
    template_name = 'blog/post_list.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
