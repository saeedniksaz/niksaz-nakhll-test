from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path("mahsoul/", views.MahsoulView.as_view()),
    path("mahsoul/discount/filter/<int:value>/", views.MahsoulRetrieveView.as_view()),
]
