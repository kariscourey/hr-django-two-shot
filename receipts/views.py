from django.shortcuts import render
from receipts.models import ExpenseCategory, Receipt, Account
from django.contrib.auth.decorators import login_required


@login_required
def list_receipts(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipt_list,
    }
    return render(request, "receipts/list.html", context)
