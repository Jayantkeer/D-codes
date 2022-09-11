from email.mime import nonmultipart
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from website.website import settings
# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email,name, password=None):
        """
        Create and save a User with the given email and password.
        """
        my_user = self.model(email=self.normalize_email(email),name=name)
        my_user.set_password(password)
        my_user.save()
        print('my user created')
        return my_user
        
class MyUser(AbstractUser):
    email=models.EmailField(max_length=100,unique=True)
    name=models.CharField(max_length=100,blank=True)
    joined_on=models.DateField(auto_now_add=True)
    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['name']
#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def _post_save_receiver(sender, **kwargs):

