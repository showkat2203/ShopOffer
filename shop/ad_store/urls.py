from django.urls import path
import ad_store

from ad_store import views

urlpatterns = [
    path('', views.index, name='index'),
]

