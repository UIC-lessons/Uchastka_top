from django.db import models
from django.utils import timezone
# Create your models here.

def media_upload_to( _instance, filename):
    return timezone.now().strftime(f"media/%Y/%M/%D{filename}")


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True        


class Media(BaseModel):
    name = models.FileField(verbose_name="Media", upload_to=media_upload_to)

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"

    def __str__(self):
        return self.name
    

class State(models.Model):
    name = models.CharField(verbose_name="State", max_length=255)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return self.name


class Region(models.Model):
    state = models.ForeignKey("common.State", on_delete = models.RESTRICT, related_name="regions")
    name = models.CharField(verbose_name="Region", max_length=200)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name
    
    
class Currency(models.Model):
    name = models.CharField(max_length=255, verbose_name="Currency Name")

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self):
        return self.name
    

class Service (models.Model):
    name = models.CharField(verbose_name="Service name", max_length=100)
    icon = models.OneToOneField("common.Media", on_delete=models.RESTRICT, verbose_name="Icon")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name
