from django.db import models
from django.contrib.auth.models import AbstractUser, User


# class TinderUser(User, AbstractUser):
#     #email = models.EmailField(max_length=60, unique=True, verbose_name="Email Address")
#     #username = models.CharField(max_length=30, unique=True, verbose_name='username')
#     #password = models.CharField(max_length=30, unique=True, verbose_name="password")
#     #is_instructor = models.BooleanField(default=False, blank=True)
#     #date_join = models.DateTimeField(auto_now=True, verbose_name="Date Joined")
#     #last_login = models.DateTimeField(auto_now=True, verbose_name="Last Login")
#     #is_active = models.BooleanField(default=False)
#     #is_staff = models.BooleanField(default=False)
#     #is_superuser = models.BooleanField(default=False)
#     def __str__(self):
#         return self.email
