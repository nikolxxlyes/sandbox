from django.db import models
# Create your models here.
class PaymentStorage(models.Model):
    CURRENCY = [
        ('EUR', 'EUR'),
        ('USD', 'USD'),
        ('GBP', 'GBP'),
        ('PLN', 'PLN'),
        ('RUB', 'RUB'),
        ('UAH', 'UAH')
    ]
    order_id = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3,
                                choices=CURRENCY,
                                default=CURRENCY[0],
                                )
    receive_currency = models.CharField(max_length=3,
                                        choices=CURRENCY,
                                        default=CURRENCY[1],
                                        )
    status = models.CharField(max_length=50,default='Send to sandbox')
    description = models.TextField(max_length=50, default='')

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f'{self.order_id} - status: {self.status}'