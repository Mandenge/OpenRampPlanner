from django.db import models

class Shift(models.Model):
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    employees = models.ManyToManyField('staff.Employee', related_name='shifts')

    def __str__(self):
        return f"{self.date} {self.time_start}-{self.time_end}"
