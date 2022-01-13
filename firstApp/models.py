from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    def __str__(self):
        return self.name

class Login(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=12)
    def __str__(self):
        return self.username


class Registration(models.Model):
    firstname = models.CharField(max_length=122,null=True)
    middlename = models.CharField(max_length=122,null=True)
    lastname = models.CharField(max_length=122,null=True)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    degree = models.CharField(max_length=12,null=True)
    semester = models.CharField(max_length=12,null=True)
    email = models.CharField(max_length=122,null=True)
    passwrd = models.CharField(max_length=12,null=True)
    phone = models.CharField(max_length=12,null=True)
    address = models.CharField(max_length=122,null=True)
    pincode =  models.CharField(max_length=12,null=True)
    city = models.CharField(max_length=122,null=True)
    photo =  models.FileField()
    signature = models.FileField()
    def __str__(self):
        return self.firstname






