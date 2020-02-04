from django.contrib import admin
from .models import PaymentStorage
# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order_id','date_added','currency','receive_currency','status']

admin.site.register(PaymentStorage,PaymentAdmin)