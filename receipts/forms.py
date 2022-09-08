from django import forms
from receipts.models import Receipt, ExpenseCategory, Account


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["vendor", "total", "tax", "date", "category", "account"]

    def __init__(self, current_user_id, *args, **kwargs):
        super(ReceiptForm, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = self.fields['account'].queryset.filter(owner_id=current_user_id)
        self.fields['category'].queryset = self.fields['category'].queryset.filter(owner_id=current_user_id)



class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ["name"]


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name", "number"]
