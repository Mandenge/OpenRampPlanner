from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    qualification = models.TextField()
    availability = models.JSONField()  # Stores availability times

    def __str__(self):
        return self.name
