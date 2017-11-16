from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^index$', views.index),
    url(r'^accueil$', views.home, name='accueil'),
    url(r'^articles$', views.articles, name='articles'),
    url(r'^article/(\d+)$', views.article, name='article'),
    url(r'^addArticle$', views.addArticle, name='addArticle'),
    url(r'^editArticle/(\d+)$', views.editArticle, name='editArticle'),
    url(r'^deleteArticle/(\d+)$', views.deleteArticle, name='deleteArticle'),
]
