from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_name/', views.get_name, name='get_name'),
]

