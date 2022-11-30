from django import forms
from ..models import Customer
class SignUpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
        self.fields['firstname'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })

        self.fields['lastname'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })

        self.fields['zipcode'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your zipcode'
        })
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your address'
        })
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your phone'
        })
    username = forms.CharField(max_length=150)
    firstname = forms.CharField(max_length=150)
    lastname = forms.CharField(max_length=150)
    email = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=150)
    zipcode = forms.CharField(max_length=150)
    address = forms.CharField(max_length=150)
    class Meta:
        model = Customer
        fields = ['username', 'firstname', 'lastname', 'email', 'password','zipcode','address','phone']
