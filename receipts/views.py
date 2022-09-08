from django.shortcuts import render
from receipts.models import ExpenseCategory, Receipt, Account


def list_receipts(request):
    receipt_list = Receipt.objects.all()
    context = {
        "receipt_list": receipt_list,
    }
    return render(request, "receipt/list.html", context)
