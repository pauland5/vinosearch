from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results/', views.results, name = 'results'),
    url(r'^details/', views.details, name = 'details'),
   ]