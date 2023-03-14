from django.db import models



class Forum(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    phone = models.BigIntegerField()
    mailid = models.TextField()
    address = models.TextField()
    district = models.TextField()
    account = models.CharField(max_length=250)

