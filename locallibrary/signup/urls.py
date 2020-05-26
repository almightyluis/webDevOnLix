from django.urls import path

from . import views

# List of directories for DJango to navigate
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.current_datetime, name='current_time'),
]