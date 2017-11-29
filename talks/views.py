# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


class TalkListDetailView(generic.View):
	def get(self, request, *args,**kwargs):
		return HttpResponse('a talk list')
