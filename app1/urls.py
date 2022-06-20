from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('ss/', views.work),
    path('time_display/', views.time),
]

