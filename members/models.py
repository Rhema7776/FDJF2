from django.db import models

# Create your models here.
class Applicant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=14)
    zip_code = models.CharField(max_length=6)
    phone = models.CharField(max_length=15)
    web = models.URLField(blank=True)
    email_address = models.EmailField(blank=True)

    def __str__(self):
        return self.name