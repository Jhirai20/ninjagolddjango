from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_gold$', views.process_gold) #no slashes in first route!
]