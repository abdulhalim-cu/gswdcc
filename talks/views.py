# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from braces import views

from . import models


class TalkListListView(
	views.LoginRequiredMixin,
	generic.ListView
	):
	models = models.TalkList

	def get_queryset(self):
		return self.request.user.lists.all()


class TalkListDetailView(generic.View):
	def get(self, request, *args,**kwargs):
		return HttpResponse('a talk list')

