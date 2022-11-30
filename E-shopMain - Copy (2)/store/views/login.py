from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')
    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        if User.objects.filter(email=email).exists():
            login(request, User.objects.get(email=email))
            return redirect("homepage")
        else:

            return redirect("signup")

def logout(request):
    request.session.clear()
    return redirect('login')
