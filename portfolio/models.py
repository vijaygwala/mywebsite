from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _



    

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""


    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

#  customize default user model as CustomUser
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()



# # Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=250,null=True)
    description=models.TextField(null=True)
    link=models.CharField(max_length=250,null=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE ,related_name='project')

    def __str__(self):
        return self.title

class Profile(models.Model):
    image = models.ImageField(upload_to='image')
    bio=models.TextField(null=True)
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE ,related_name='profile')
    resume=models.FileField(null=True,blank=True)
    def __str__(self):
        return self.bio
class Skill(models.Model):
    choice=(
         ('B', 'Begginer'),
        ('I', 'Intermediate'),
        ('A', 'Advance')

    )
    name=models.CharField(max_length=250,null=True,blank=True)
    level=models.CharField(max_length=250,choices=choice,null=True,blank=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE ,related_name='skill')



class Contact(models.Model):
    #user=models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='contact' )
    name=models.CharField(max_length=250,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    message=models.TextField(null=True,blank=True)




