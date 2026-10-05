from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_view, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="main/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("booking/", views.booking_view, name="booking"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path(
        "booking/<int:pk>/cancel/",
        views.cancel_booking,
        name="cancel_booking"
    ),
]
