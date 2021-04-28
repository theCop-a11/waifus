from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def blog(request):

    posts= Post.objects.all() # pylint: disable=maybe-no-member
    return render(request, "blog/blog.html", {"posts":posts})

def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id) # pylint: disable=maybe-no-member
    posts = Post.objects.filter(categorias = categoria) # pylint: disable=maybe-no-member

    return render(request, "blog/categoria.html", {'categoria': categoria, "posts":posts})



