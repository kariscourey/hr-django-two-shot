from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from receipts.views import (
    list_receipts,
    create_receipts,
    list_categories,
    list_accounts,
)

urlpatterns = [
    path("", list_receipts, name="home"),
    path("create/", create_receipts, name="create_receipt"),
    path("categories/", list_categories, name="list_category"),
    path("accounts/", list_accounts, name="list_account"),
]
