from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

    def __str__(self) -> str:
        return self.username

    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
