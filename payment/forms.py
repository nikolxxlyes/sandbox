from django import forms
from .models import PaymentStorage

class PaymentForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 20}))
    class Meta:
        model = PaymentStorage
        fields = ['price', 'currency','receive_currency','description']
        labels = {'price': "Amount", 'currency': "Base currency",
                  'receive_currency': "Receive currency","description":"Description" }

