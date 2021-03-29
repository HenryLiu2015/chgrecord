from django.db import models


# Create your models here.
class ChgRecord(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    lineId = models.CharField(max_length=10, default='Q000')
    deviceName = models.CharField(max_length=120, null=False)
    loopNo = models.CharField(max_length=50, null=False)
    opeContent = models.CharField(max_length=256, null=False)
    opeReason = models.CharField(max_length=256, null=False)
    opeDate = models.DateField(null=False)
    adjValueBefore = models.FloatField(default=0.0)
    adjValueAfter = models.FloatField(default=0.0)
    adjValueUnit = models.CharField(max_length=10)
