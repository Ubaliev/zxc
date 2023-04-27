from django.db import models

# Create your models here.
class Car(models.Model):

    name = models.CharField(max_length=30)
    max_speed = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=127)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date_issue = models.DateField()
