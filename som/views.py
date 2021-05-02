from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse


def index(request):
    context = {}
    return TemplateResponse(request, "som/index.html", context=context)