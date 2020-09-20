from django.shortcuts import render

from django.views.generic import TemplateView

class HomeVew(TemplateView) : 
    template_name = 'home.html'

class AboutVew(TemplateView) : 
    template_name = 'about.html'