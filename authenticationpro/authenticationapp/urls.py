from django.urls import path, include
from .views import signUp, home

urlpatterns = [
    path('signUp/' , signUp, name = 'signUp'),
    path('', home, name = 'home'),
    path("accounts/", include("django.contrib.auth.urls")),
]