from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('profiles/', views.ProfileView.as_view()),
]
