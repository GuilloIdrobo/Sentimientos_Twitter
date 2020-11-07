from django.shortcuts import render
from django.views.generic import TemplateView

class Sentimientos_View(TemplateView):
    template_name="index.html"