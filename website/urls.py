from django.urls import path
from .views import (
    IndexView,
    ContactView,
    CreateTeam,
    TermsView,
    CountdownView,
)

app_name = "website"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contact", ContactView.as_view(), name="contact"),
    path("register", CreateTeam.as_view(), name="register"),
    path("terms", TermsView.as_view(), name="terms"),
    path("countdown", CountdownView.as_view(), name="countdown"),
]
