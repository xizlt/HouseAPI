from django.contrib import admin
from .models import Payment, Accrued


@admin.register(Accrued)
class AccruedAdmin(admin.ModelAdmin):
    list_display = ('user', 'accrued', 'payment', 'created')
    fields = ('user', 'accrued', 'payment')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'sum', 'created')
    fields = ('user', 'sum')
