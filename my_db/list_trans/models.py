from django.db import models
from tasks.models import Tasks


class Carrier(models.Model):
    company_name = models.CharField(max_length=30)
    telephone = models.IntegerField(default=0)
    ati = models.IntegerField(default=0)
    direction = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name

class EditCarrier(models.Model):
    carrier = models.ForeignKey(Carrier, null=True, on_delete=models.CASCADE)
    tasks = models.ForeignKey(Tasks, null=True, on_delete=models.CASCADE)
    brand_and_number_car = models.CharField(max_length=50)
    name_driver = models.CharField(max_length=50)
    price_carrier = models.IntegerField(default=0)





