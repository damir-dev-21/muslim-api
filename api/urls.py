from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.RegisterUserView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('points/', views.GetPointsView.as_view()),   
]
