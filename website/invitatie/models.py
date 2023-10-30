
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    num_of_people = models.IntegerField()
    additional_name = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'






