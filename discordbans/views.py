from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic


class TopPageView(generic.TemplateView):
    template_name = "index.html"
