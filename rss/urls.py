from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('rss/business', views.index, name='index'),
]
