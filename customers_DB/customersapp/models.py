from django.db import models

# Create your models here.

class Customer(models.Model):
    Name = models.CharField(max_length = 300)
    address = models.CharField(max_length = 300)
    contact_number = models.CharField(max_length=12)
    emailaddress = models.EmailField(max_length = 300)
    
    def getName(self):
        return self.Name
    
    def __str__(self):
        return str(self.pk) + ": " + str(self.Name) + "," + str(self.address) + ", " + str(self.contact_number) + ", " + str(self.emailaddress) 


class Account(models.Model):
    username = models.CharField(max_length=250, unique = True)
    password = models.CharField(max_length=250)
    # objects = models.Manager()

    def getUsername(self):
        return f"{self.username}"

    def getPassword(self):
        return f"{self.password}"

    def __str__(self):
        return f"{self.pk}: {self.username}"