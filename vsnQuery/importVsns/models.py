from django.db import models

class VSNData(models.Model):
    Indexed_SNP = models.CharField(max_length=100)	
    SerialNumberPattern = models.CharField(max_length=12)
    VehicleTrimId = models.IntegerField()
    Year = models.IntegerField()
    Make = models.CharField(max_length=3)
    Model = models.CharField(max_length=200)
    TrimName = models.CharField(max_length=20)

    def __str__(self):              # __unicode__ on Python 2
    	return self.SerialNumberPattern

