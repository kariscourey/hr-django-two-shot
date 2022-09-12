from django.contrib import admin
from receipts.models import ExpenseCategory, Receipt, Account, Car  # Pat


class ExpenseCategoryAdmin(admin.ModelAdmin):
    pass


class ReceiptAdmin(admin.ModelAdmin):
    pass


class AccountAdmin(admin.ModelAdmin):
    pass


# class PatAdmin(admin.ModelAdmin):
#     pass


class CarAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Account, AccountAdmin)
# admin.site.register(Pat, PatAdmin)
admin.site.register(Car, CarAdmin)
