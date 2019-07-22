from django.db import models

class Municipality(models.Model):
    STATE_OPTIONS = (
        ('A', 'Active'),
        ('U', 'Unactive')
    )
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    state = models.CharField(max_length=1, choices=STATE_OPTIONS)

    def __str__(self):
        return self.name

class Region(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    municipalities = models.ManyToManyField(Municipality, through='MunicipalityXRegion')

    def __str__(self):
        return self.name

class MunicipalityXRegion(models.Model):
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)