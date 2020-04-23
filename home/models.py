from django.db import models
from django import forms
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class Producer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    picture = models.ImageField(upload_to='media/',
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    price = models.IntegerField()
    name = models.CharField(max_length=50)
    date_added = models.DateField(default=datetime.now())
    weight = models.IntegerField()
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return f"{self.price}, {self.name}, {self.date_added}, {self.weight}, {self.producer}"


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.BooleanField()
    number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
