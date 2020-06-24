from django.urls import path

from app import views

urlpatterns = [
    path('auth/', views.AuthView.as_view()),
    path('order/', views.OrderView.as_view()),
]
