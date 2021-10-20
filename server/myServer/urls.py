from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tasks', views.tasks, name='tasks'),
    path('maps', views.maps, name='maps'),
    path('profile', views.profile, name='profile'),
]
