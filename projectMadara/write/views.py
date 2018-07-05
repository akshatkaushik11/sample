# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Responsible for converting description into sharable text.
from urllib.parse import quote_plus
from .forms import TotoForm
from .models import Toto

from django.utils import timezone
from django.db.models import Q

from accounts.models import UserAccount

def toto_create(request):
	"""
		This makes sure that the form accpets a POST requests (of some data) or Nothing.
		Without this the form would even accept empty totos.
	"""
	if not request.user.is_authenticated():
		raise Http404

	form = TotoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		filter_content(instance.content)
		instance.user = request.user
		instance.save()
		messages.success(request, "Toto created!")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Something went wrong", extra_tags="") 
	context = {
		'title': "Create",
		'form' : form,
	}
	return render(request, 'write/write.html', context)

def toto_detail(request, slug):
	instance 		= get_object_or_404(Toto, slug=slug)

	if instance.publish > timezone.now() or instance.draft:
		if not request.user == instance.user:
			raise Http404
	share_string = quote_plus("Hey! I've just started learning from gitall.tech. It's cool. Check them out!!!")
	context = {
		'instance'		: instance,
		'title'			: "Details",
		'share_string' 	: share_string,
	}

	return render(request, 'write/detail.html', context)

def toto_edit(request, slug):
	# This retuns the data (for form) the particular toto 
	instance = get_object_or_404(Toto, slug=slug)

	if not request.user == instance.user:
		raise Http404

	# if not request.user.is_superuser or not request.user.is_staff:
	# 	raise Http404

	"""
		without instance=instance part, the form would be an empty form
		instance=instance essentially adds value of the instance to the form
	"""
	form = TotoForm(request.POST or None, request.FILES or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Edited nicely!")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Something didn't edit.", extra_tags="") 

	context = {
		'title': "Edit",
		'instance' : instance,
		'form': form,
	}
	return render(request, 'write/edit.html', context)

def toto_list(request):
	# queryset_list = Toto.objects.all().order_by("-timestamp")
	# queryset_list = Toto.objects.filter(draft=False).filter(publish__lte=timezone.now())
	# the above command is implemented by using 
	queryset_list = Toto.objects.active()

	query = request.GET.get('query')
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query) |
				Q(content__icontains=query) |
				Q(user__first_name__icontains=query)|
				Q(user__last_name__icontains=query)).distinct()

	paginator = Paginator(queryset_list, 1)

	page = request.GET.get('page')
	
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		queryset_list = paginator.page(1)
	except EmptyPage:
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"toto_list" : queryset_list,
		"title" : "List",
	}
	# if request.user.is_authenticated():
	# 	context = {
	# 		"tut_list" : queryset,
	# 		"title": "my list",
	# 	}
	# else:
	# 	context = {
	# 		'title' : "list"
	# 	}
	return render(request, 'write/list.html', context)

def toto_delete(request, slug):
	instance = get_object_or_404(Toto, slug=slug)
	if not request.user == instance.user:
		raise Http404
	instance.delete()
	context = {
		'title': "Delete",
	}
	# messages.success(request, "Deteted")
	return redirect("toto:list")

def toto_draft(request):
	query = Toto.objects.draft()

	context = {
		'draft_list' : query,
	}

	return render(request, 'write/draft_list.html', context)

def filter_content(content):
	print(content)