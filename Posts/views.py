from django.shortcuts import get_object_or_404, render
from .models import Post
# Create your views here.
def list_view(request):
    posts = Post.objects.all()
    return render(request,"post_list.html",{'posts':posts})

def detail_view(request,pk):
    post= get_object_or_404(Post,pk=pk)
    return render(request,"post_detail.html",{'post':post})
