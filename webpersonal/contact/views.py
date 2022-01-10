from django.shortcuts import render
from django.views.generic.base import TemplateView


class ContactPageView(TemplateView):
    template_name = 'contact/contact.html'
