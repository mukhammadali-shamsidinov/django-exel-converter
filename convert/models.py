from django.db import models

# Create your models here.
class UserData(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone_number= models.IntegerField()
    adress = models.TextField()

    def __str__(self):
        return self.fname