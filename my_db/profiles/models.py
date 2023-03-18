from django.db import models
from django.contrib.auth.models import User
import time


POST_CHOICES = (
    ('Менеджер', 'Менеджер'),
    ('Логист', 'Логист'),
    ('Руководитель', 'Руководитель'),
    ('Стажер','Стажер')   
)

class UserInformation(models.Model):
    profile = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    bio = models.TextField(max_length=250, blank=True)
    post = models.CharField(max_length=30, choices=POST_CHOICES, default='Стажер')
    status = models.BooleanField(default=False)
    profile_image = models.ImageField(
        upload_to='profile_images/',
        default='profile_images/default_profile.jpg',
        null=True,
        blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
    

