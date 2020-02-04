from django.shortcuts import render
from django.views.generic import View
from .forms import PaymentForm
from .models import PaymentStorage
from django.conf import settings
import requests
from datetime import datetime

class ButtonView(View):
    template_name = 'button.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,)

class PaymentView(View):
    template_name = 'payment.html'

    def get(self, request,*args, **kwargs):
        form = PaymentForm()
        context = {'form': form}
        return render(request,self.template_name,context)

    def post(self, request,*args, **kwargs):
        form = PaymentForm(data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.order_id = 'CGORDER-' + str(len(PaymentStorage.objects.all()) + 1)
            res = F'Success. New order "{new_order.order_id}" is registered.'
            new_order.save()
            self.send_order(new_order)
        else:
            res = 'Error. Invalid data.'
        context = {'res': res}
        return render(request, self.template_name, context)

    def send_order(self,order):
        params = {
            'price_amount': str(order.price),
            'price_currency': order.currency,
            'receive_currency': order.receive_currency,
            'callback_url': 'https://'+settings.ALLOWED_HOSTS[0]+'/callback?id={}'.format(order.order_id),
            'title': order.order_id,
            'order_id': order.order_id,
            'description': order.description
        }
        # print(params)
        requests.post('https://api-sandbox.coingate.com/v2/orders',params=params,
                      headers=settings.MY_SETTINGS['SANDBOX_HEAD'])


class HistoryView(View):
    template_name = 'history.html'
    def get(self, request, *args, **kwargs):
        # orders = PaymentStorage.objects.all()
        context = {'orders': self.get_history()}
        return render(request, self.template_name, context)

    def get_history(self):
        r = requests.get('https://api-sandbox.coingate.com/v2/orders?per_page=20&page=1',
                         headers=settings.MY_SETTINGS['SANDBOX_HEAD'])
        if r.status_code == 200:
            req = r.json()
        print(r.json())
        orders = []
        for order in req['orders']:
            some_order = {
                'status':order['status'],
                'price_currency':order['price_currency'],
                'price_amount':order['price_amount'],
                'receive_currency':order['receive_currency'],
                'created_at': datetime.strptime(order['created_at'],'%Y-%m-%dT%H:%M:%S+00:00'),
                'order_id': order['order_id'] if order['order_id'] else 'Button payment',
                'payment_url':order['payment_url'],
            }
            orders.append(some_order)
        return orders
