from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('list/', views.viewlist, name='view_list'),
    path('', views.index, name='index'),
    path('abc/', views.ham1, name='ham1'),
]