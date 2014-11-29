from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Category, Label, Post

def index(request, page=1):
	posts = Post.objects.filter(published=True)
	paginator = Paginator(posts, 5)
	return render(request, 'blog/index.html', {
		'posts': paginator.page(page),
	})

def category(request, category_slug, page=1):
	category = Category.objects.get(slug=category_slug)
	posts = Post.objects.filter(category=category.id, published=True)
	paginator = Paginator(posts, 5)
	return render(request, 'blog/index.html', {
		'posts': paginator.page(page),
	})

def read(request, post_slug):
	post = Post.objects.get(slug=post_slug, published=True)
	return render(request, 'blog/read.html', {
		'post': post,
	})
