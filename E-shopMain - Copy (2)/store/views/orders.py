from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from django.views import generic
from django.urls import reverse_lazy
class OrderView(View):
    def get(self , request ):
        customer = Customer.objects.get(user=request.user)
        orders = Order.get_orders_by_customer(customer)
        return render(request , 'orders.html'  , {'orders' : orders})
