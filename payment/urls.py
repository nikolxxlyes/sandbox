from django.urls import path
from . import views

app_name = 'payment'
urlpatterns = [
    path('', views.PaymentView.as_view(), name='new_payment'),
    path('button', views.ButtonView.as_view(), name='button'),
    path('payment', views.PaymentView.as_view(), name='new_payment'),
    path('history', views.HistoryView.as_view(), name='history'),
]