from django.db import models


class Person(models.Model):
    name = models.CharField(null=False, max_length=100)
    surname = models.CharField(null=False, max_length=100)
    date_added = models.DateField(null=False, auto_now_add=True)
    date_updated = models.DateField(null=False, auto_now=True)

class Counter(models.Model):
    counter_value = models.PositiveIntegerField(default=1)