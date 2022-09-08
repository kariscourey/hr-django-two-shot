from django.shortcuts import render, redirect
from receipts.models import ExpenseCategory, Receipt, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm, ExpenseCategoryForm


@login_required
def list_receipts(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipt_list,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipts(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.purchaser = request.user
            item.save()
        return redirect("home")
    else:
        form = ReceiptForm()

    context = {
        "form": form
    }

    return render(request, "receipts/create.html", context)


@login_required
def list_categories(request):
    category_list = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "category_list": category_list,
    }
    return render(request, "categories/list.html", context)


@login_required
def list_accounts(request):
    account_list = Account.objects.filter(owner=request.user)
    context = {
        "account_list": account_list,
    }
    return render(request, "accounts/list.html", context)


@login_required
def create_categories(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
        return redirect("list_categories")
    else:
        form = ExpenseCategoryForm()

    context = {
        "form": form
    }

    return render(request, "categories/create.html", context)
