from django.urls import path
from .views import RegisterView, LoginView, WhoView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('who/', WhoView.as_view()),
]