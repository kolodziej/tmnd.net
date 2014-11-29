from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.template import RequestContext, loader
from download.models import Platform, Version, File

def index(request):
	platforms = Platforms.objects.all();
	return render(request, 'download/index.html', {
		'platforms': platforms,
	});
