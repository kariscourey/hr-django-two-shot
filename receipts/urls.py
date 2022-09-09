from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from receipts.views import (
    # list_receipts,
    # create_receipts,
    # list_categories,
    # list_accounts,
    # create_categories,
    # create_accounts,

    ReceiptListView,
    ReceiptCreateView,
    CategoryListView,
    AccountListView,
    CategoryCreateView,
    AccountCreateView,
)

urlpatterns = [
    # path("", list_receipts, name="home"),
    # path("create/", create_receipts, name="create_receipt"),
    # path("categories/", list_categories, name="list_categories"),
    # path("accounts/", list_accounts, name="list_account"),
    # path("categories/create/", create_categories, name="create_category"),
    # path("accounts/create/", create_accounts, name="create_account"),

    path("", ReceiptListView.as_view(), name="home"),
    path("create/", ReceiptCreateView.as_view(), name="create_receipt"),
    path("categories/", CategoryListView.as_view(), name="list_categories"),
    path("accounts/", AccountListView.as_view(), name="list_account"),
    path("categories/create/", CategoryCreateView.as_view(), name="create_category"),
    path("accounts/create/", AccountCreateView.as_view(), name="create_account"),
]
