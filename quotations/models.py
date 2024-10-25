from django.db import models

class Quotation(models.Model):
    customer_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    quotation_number = models.IntegerField()
    car_type = models.CharField(max_length=10, choices=[('new', 'New'), ('used', 'Used')])
    cpr = models.CharField(max_length=11)
    date = models.DateField()
    to = models.CharField(max_length=10, choices=[('NBB', 'NBB'), ('BBK', 'BBK'), ('AUB', 'AUB'), 
                                                  ('BCFC', 'BCFC'), ('NFH', 'NFH'), ('BISB', 'BISB')])
    car_brand = models.CharField(max_length=50)
    chassis_no = models.CharField(max_length=50)
    engine_no = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    downpayment = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Quotation #{self.quotation_number} - {self.customer_name}"

# models.py
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # You might want to store hashed passwords
    privileges = models.CharField(max_length=50)  # e.g., 'both', 'admin', 'user'

    def __str__(self):
        return self.username