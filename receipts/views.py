# from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from receipts.models import ExpenseCategory, Receipt, Account
# from django.contrib.auth.decorators import login_required
# from receipts.forms import ReceiptForm, ExpenseCategoryForm, AccountForm

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required
# def list_receipts(request):
#     receipt_list = Receipt.objects.filter(purchaser=request.user)
#     context = {
#         "receipt_list": receipt_list,
#     }
#     return render(request, "receipts/list.html", context)


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"
    context_object_name = "receipt_list"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)


# @login_required
# def create_receipts(request):
#     user = request.user
#     if request.method == "POST":
#         form = ReceiptForm(request.POST, current_user=user)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.purchaser = request.user
#             item.save()
#         return redirect("home")
#     else:
#         form = ReceiptForm(current_user=user)

#     context = {"form": form}

#     return render(request, "receipts/create.html", context)


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    template_name = "receipts/create.html"
    fields = ["vendor", "total", "tax", "date", "category", "account"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = self.request.user
        form.instance.purchaser = user
        return super().form_valid(form)

    # TODO
    def get_form(self, *args, **kwargs):
        form = super(ReceiptCreateView, self).get_form(*args, **kwargs)
        form.fields['category'].queryset = Receipt.objects.filter(purchaser=self.request.user)
        form.fields['account'].queryset = Receipt.objects.filter(purchaser=self.request.user)
        return form


# @login_required
# def list_categories(request):
#     category_list = ExpenseCategory.objects.filter(owner=request.user)
#     context = {
#         "category_list": category_list,
#     }
#     return render(request, "categories/list.html", context)


class CategoryListView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = "categories/list.html"
    context_object_name = "category_list"

    def get_queryset(self):
        return ExpenseCategory.objects.filter(owner=self.request.user)


# @login_required
# def list_accounts(request):
#     account_list = Account.objects.filter(owner=request.user)
#     context = {
#         "account_list": account_list,
#     }
#     return render(request, "accounts/list.html", context)


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "accounts/list.html"
    context_object_name = "account_list"

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)


# @login_required
# def create_categories(request):
#     if request.method == "POST":
#         form = ExpenseCategoryForm(request.POST)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.owner = request.user
#             item.save()
#         return redirect("list_categories")
#     else:
#         form = ExpenseCategoryForm()

#     context = {"form": form}

#     return render(request, "categories/create.html", context)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    template_name = "categories/create.html"
    fields = ["name"]
    success_url = reverse_lazy("list_categories")

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


# @login_required
# def create_accounts(request):
#     if request.method == "POST":
#         form = AccountForm(request.POST)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.owner = request.user
#             item.save()
#         return redirect("list_account")
#     else:
#         form = AccountForm()

#     context = {"form": form}

#     return render(request, "accounts/create.html", context)


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "accounts/create.html"
    fields = ["name", "number"]
    success_url = reverse_lazy("list_account")

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)
