from django import forms
from receipts.models import Receipt, ExpenseCategory, Account


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["vendor", "total", "tax", "date", "category", "account"]

    def __init__(self, *args, **kwargs):
        # form = super(Receipt, self).get_form(*args, **kwargs)
        # form.fields['categories'].queryset = Category.objects.filter(profile=self.request.user.profile)
        # return form

        current_user = kwargs.pop('current_user', None)
        super(ReceiptForm, self).__init__(*args, **kwargs)
        if current_user:
            self.fields['account'].queryset = self.fields['account'].queryset.filter(owner_id=current_user.id)
            self.fields['category'].queryset = self.fields['category'].queryset.filter(owner_id=current_user.id)



class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ["name"]


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name", "number"]
