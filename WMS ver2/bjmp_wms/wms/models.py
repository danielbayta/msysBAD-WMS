from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 300)
    address = models.CharField(max_length = 300)
    contact_number = models.CharField(max_length=13)
    email = models.EmailField(max_length = 300)
    
    def getName(self):
        return self.name 
    
    def __str__(self):
        return str(self.pk) + ": " + str(self.name) 

