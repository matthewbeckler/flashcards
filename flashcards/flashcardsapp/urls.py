from django.urls import path

from . import views # this imports views.py in the flashcardsapp app, so we can use views.index below

urlpatterns = [
    path('', views.index, name='index')
]

