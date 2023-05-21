from django.db import models

# Create your models here.

class UserSignIn(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    mobileno = models.CharField(max_length=10)
    password = models.CharField(max_length=46)
    cookiekey = models.CharField(max_length=45, default='0')
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    bloodgroup = models.CharField(max_length=3)
    doorno = models.CharField(max_length=6, blank=True, null=True)
    line1 = models.CharField(max_length=50, blank=True, null=True)
    line2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name
    