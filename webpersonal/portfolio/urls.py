from django.urls import path
from .views import PortfolioPageView

app_name= 'portfolio'
urlpatterns = [
    path('', PortfolioPageView.as_view(), name='home')
]
