from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^index$', views.index),
    url(r'^accueil$', views.home),
    url(r'^articles$', views.articles),
    url(r'^article/(\d+)$', views.lire, name='lire')

]
