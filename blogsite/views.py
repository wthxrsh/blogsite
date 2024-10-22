from django.shortcuts import render
from blog.models import blogcontent
from django.shortcuts import render, get_object_or_404
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def support(request):
    return render(request, 'support.html')

def all_blogs(request):
  blogs = blogcontent.objects.all()
  return render(request, 'blogs.html', {'blogs': blogs})


def blog_detail(request, blog_id):
  blog = get_object_or_404(blogcontent, pk=blog_id)
  return render(request, 'blog_detail.html', {'blog': blog})