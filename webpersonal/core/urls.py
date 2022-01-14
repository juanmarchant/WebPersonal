from django.urls.conf import path
from .views import HomePageView
from django.views.generic import TemplateView

app_name='main'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('robots.txt', TemplateView.as_view(template_name='core/robots.txt', content_type='text/plain')),
]
