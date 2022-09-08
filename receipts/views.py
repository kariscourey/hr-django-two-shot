from django.shortcuts import render, redirect
from receipts.models import ExpenseCategory, Receipt, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm


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
