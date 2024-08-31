from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
