from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', blank=True,  null=True,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f'{self.user}'
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
User.userprofile = property(lambda u:Customer.objects.get_or_create(user=u)[0])
