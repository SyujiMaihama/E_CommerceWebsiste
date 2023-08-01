from django.db import models
from .products import Products
from .customer import Customer
import datatime

class Oder(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                on_delete=models.CASCADE)
    quantity = models.IntergerField(default=1)
    price = models.IntergerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)#default, today's date
    status = models.BooleanField(default=False)#To finish filling or not?

    def placeOrder(self):
        self.save

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
