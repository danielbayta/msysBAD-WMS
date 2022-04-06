from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 300, null=True)
    address = models.CharField(max_length = 300, null=True)
    contact_number = models.CharField(max_length=13, null=True)
    email = models.EmailField(max_length = 300, null=True)
    objects = models.Manager()
    
    def getName(self):
        return self.name 
    
    def __str__(self):
        return str(self.pk) + ": " + str(self.name) 

LEVELS = (
    ('Urgent', 'Urgent'),
    ('High', 'High'),
    ('Low', 'Low'),
    ('No Need', 'No Need'),
)

TYPES = (
    ('Type 1','Type 1'),
    ('Type 2','Type 2'),
    ('Type 3','Type 3'),
)

class Inventory(models.Model):
    name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, choices=TYPES, null=True)
    description = models.CharField(max_length=100, null=True)
    unit_price = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    reorder_level = models.CharField(max_length=100, choices=LEVELS, null=True)
    reorder_date = models.DateTimeField()
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ": " + str(self.name) + ", " + str(self.type)