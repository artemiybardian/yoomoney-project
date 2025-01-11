from django.contrib import admin
from .models import Phone, Transaction

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'provider', 'amount', 'payment_day')
    search_fields = ('phone_number', 'provider')
    list_filter = ('provider',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('phone', 'amount', 'status', 'created_at', 'yoomoney_transaction_id')
    search_fields = ('phone__phone_number', 'yoomoney_transaction_id')
    list_filter = ('status', 'created_at')
