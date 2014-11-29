from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.template import RequestContext, loader
from blog.models import Category, Label, Post

def index(request):
	posts = Post.objects.filter(published=True)
	return render(request, 'blog/index.html', {
		'posts': posts,
	})

def category(request, category_slug):
	category = Category.objects.get(slug=category_slug)
	posts = Post.objects.filter(category=category.id, published=True)
	return render(request, 'blog/index.html', {
		'posts': posts,
	})

def read(request, post_slug):
	post = Post.objects.get(slug=post_slug, published=True)
	return render(request, 'blog/read.html', {
		'post': post,
	})
