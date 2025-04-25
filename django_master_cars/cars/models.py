from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')
    factory_year = models.IntegerField(max_length=4, blank=True, null=True)
    model_year = models.IntegerField(max_length=4, blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    photo = models.ImageField(upload_to='cars/photos/', blank=True, null=True)

    def __str__(self):
        return self.model
