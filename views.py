from django.shortcuts import render
from .models import blogcontent
# Create your views here.
def all_blogs(request):
  blogs = blogcontent.objects.all()
  return render(request, 'blog/blogs.html', {'blogs': blogs})