from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
]
