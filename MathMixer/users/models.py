from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Аватар')


    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username



