from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from django.views import generic
from django.urls import reverse_lazy
#
# @login_required
# def profile(request):
#     return render(request, 'userprofile.html')


class Profile( generic.View):

    template_name = "userprofile.html"

    def get(self, request):
         return render(request, 'userprofile.html')


    def get_object(self):
        return self.request.user
