from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Project

# Create your views here.

class PortfolioPageView(TemplateView):
    template_name = 'portfolio/portfolio.html'

    def get_context_data(self):
        context = {
        'projects': Project.objects.all(),
        }
        return context
    
