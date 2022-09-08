from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from receipts.views import (
    list_receipts,
)

urlpatterns = [
    path("", list_receipts, name="home"),
]
