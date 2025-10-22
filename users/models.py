from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPE_CHOICES = [
    ('doctor', 'Doctor'),
    ('patient', 'Patient'),
]

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
