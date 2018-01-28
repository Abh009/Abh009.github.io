from django.shortcuts import render, get_object_or_404
from app.models import *

# Create your views here.


def home(request):
    return render(request,"index.html",{})

def show_article(request,article_id):
    article = get_object_or_404(Article, pk = article_id)
    if not article:
        raise Http404("Article not found")
    message = {'article_name':article.headline, 'article_content':article.content, 'author':article.author}
    return render(request,"index.html",message)