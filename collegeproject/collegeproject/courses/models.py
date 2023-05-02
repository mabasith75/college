from django.db import models

# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    purpose = models.TextField()
    materials = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)