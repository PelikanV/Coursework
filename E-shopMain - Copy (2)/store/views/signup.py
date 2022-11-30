from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from ..models.customer import Customer
from django.contrib.auth.models import User
from ..forms.forms import SignUpForm
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form["username"].value()
            firstname = form["firstname"].value()
            lastname = form["lastname"].value()
            email = form["email"].value()
            address = form["address"].value()
            zipcode = form["zipcode"].value()
            phone = form["phone"].value()
            password = form["password"].value()
            form.save()
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()
            login(request, user)

            customer=Customer.objects.create(
                user = user,
                firstname = firstname,
                lastname = lastname,
                address = address,
                zipcode =zipcode,
                phone = phone
            )

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

