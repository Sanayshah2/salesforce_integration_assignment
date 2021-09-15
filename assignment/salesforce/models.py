from django.db import models
from django.db.models.fields import EmailField
from django.utils import timezone


class Users(models.Model):
    username = models.CharField(max_length=100, default='', verbose_name='Your Username')
    name = models.CharField(max_length=30, default='', verbose_name='Your Full Name')
    user_id = models.CharField(max_length=30, default='', unique=True)
    email = models.EmailField(max_length=15, default='')
    created_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"

class Account(models.Model):
    account_id = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=30, default='', verbose_name='Account Name')
    created_date = models.DateTimeField()
    user_id = models.CharField(max_length=30, default='')

    def __str__(self):
        return f"{self.name}"

class Contact(models.Model):
    contact_id = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=30, default='', verbose_name='Contact Name')
    account_id = models.CharField(max_length=30, default='')
    user_id = models.CharField(max_length=30, default='')
    created_date = models.DateTimeField()


    def __str__(self):
        return f"{self.name}"
