from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.common.models import BaseModel
from apps.estate.estatechoices import EstateStatusChoices



class Estate_Agent(BaseModel):
    name = models.CharField(verbose_name="Agent name", max_length=50)
    last_name = models.CharField(verbose_name="Agent last name", max_length=50)
    bio = models.TextField(verbose_name="Agent bio", blank=True, null=True)
    avatar = models.ManyToManyField("common.Media", verbose_name = "Avatar",blank=True, related_name="agents")
    phone = models.CharField(verbose_name="phone", max_length=255)
    mobile = models.CharField(verbose_name="mobile phone", max_length=255, null=True, blank=True)
    email = models.EmailField(verbose_name="Email")
    telegram = models.CharField(max_length=255, verbose_name="Telegram", blank=True, null=True)
    whatsapp = models.CharField(max_length=255, verbose_name="WhatsApp", blank=True, null=True)
    instagram = models.CharField(max_length=255, verbose_name="Instagram", blank=True, null=True)
    facebook = models.CharField(max_length=255, verbose_name="Facebook", blank=True, null=True)
    x = models.CharField(max_length=255, verbose_name="X", blank=True, null=True)

    class Meta:
        verbose_name = "Estate Agent"
        verbose_name_plural = "Estate Agents"

    def __str__(self):
        return f"{self.name} {self.last_name}"
    

class Estate(BaseModel):
    name = models.CharField(verbose_name="Estate Name", max_length=100)
    agent = models.ForeignKey("estate.Estate_agent", on_delete=models.RESTRICT, verbose_name="Agent", related_name="estates", default=1)
    category = models.ForeignKey("estate.EstateCategory", on_delete=models.RESTRICT, verbose_name="Estate category", related_name="estates")
    state = models.ForeignKey("common.State", on_delete=models.RESTRICT, related_name="estates")
    region = models.ForeignKey("common.Region", on_delete=models.RESTRICT, related_name="estates0")
    address = models.CharField(max_length=150, verbose_name="Estate address", default="earth")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")
    status = models.CharField(verbose_name="Status", choices=EstateStatusChoices.choices, max_length=100)
    area = models.DecimalField(verbose_name="Area m^2", max_digits=7, decimal_places=2)
    beds = models.IntegerField(verbose_name="Bedrooms", validators=[MaxValueValidator(12), MinValueValidator(0)])
    bath = models.IntegerField(verbose_name="Bathrooms", validators=[MaxValueValidator(15), MinValueValidator(0)])
    garage = models.IntegerField(verbose_name="Garage", validators=[MaxValueValidator(5), MinValueValidator(0)])
    price = models.DecimalField(verbose_name="Price", max_digits=15, decimal_places=2)
    currency = models.ForeignKey("common.Currency", on_delete=models.RESTRICT, related_name="estates")
    description = models.TextField(verbose_name="Estate description")
    amenities = models.ManyToManyField("estate.Amenities", verbose_name="Amenities", related_name="estates")
    images = models.ManyToManyField("common.Media", verbose_name="Images", related_name="estates")
    video = models.URLField(verbose_name="Video", blank=True, null=True)

    class Meta :
        verbose_name = "Estate"
        verbose_name_plural = "Estates"

    def __str__(self):
        return f"{self.name}, {self.price}"


class EstateCategory(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Estate Category Name")

    class Meta:
        verbose_name = "Estate Category"
        verbose_name_plural = "Estate Categories"

    def __str__(self):
        return self.name


class Amenities(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Amenity Name")

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"

    def __str__(self):
        return self.name


class EstateAgentComment(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    comment = models.TextField(verbose_name="Comment")

    class Meta:
        verbose_name = "Estate Agent Comment"
        verbose_name_plural = "Estate Agent Comments"

    def __str__(self):
        return self.name