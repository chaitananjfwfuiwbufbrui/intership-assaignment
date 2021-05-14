from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.base import Model
from home import settings
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    Name = models.CharField(max_length=255)
    # user_id =models.AutoField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Name']


    
    def __str__(self):
        return self.email


# <----------------model for advisor-------------------------->

class advisor(models.Model):
    
    advisor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,blank=True,null=True)
    advisor_name =  models.CharField( max_length=50)
    image_urls = models.CharField( max_length=150)   
# <----------------model for booking --------------------------->
class Booking_call(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,blank=True,null=True)
    Adviser= models.ForeignKey(advisor,on_delete=models.SET_NULL,blank=True,null=True)
    Booking_time = models.CharField( max_length=150)   
