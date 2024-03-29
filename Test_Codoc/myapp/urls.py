from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('health/', views.health, name='health'),
    path('key/', views.get_key, name='get_key'),
    path('decode/', views.decode_message, name='decode_message'),
    path('encode/', views.encode_message, name='encode_message'),  # Nouvel endpoint
]
