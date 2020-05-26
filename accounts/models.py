from django.conf import settings  
from django.db.models.signals import post_save     
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser 
)
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from .utils import code_generator

USERNME_REGEX = '^[a-zA-Z0-9.@-_]*$'  

# custom authentication 
class MyUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username, 
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True 
        user.save(using=self._db) 
        return user



class MyUser(AbstractBaseUser):
    username = models.CharField(
        max_length=120, unique=True, validators=[
            RegexValidator(
                regex = USERNME_REGEX,
                message = "Username must be Alphanumeric of contain any of the following: ' . @ _ - ' ", 
                code = 'invalid_username',
            ) 
        ]
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    zipcode = models.CharField(max_length=120, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False) 

    objects = MyUserManager()

    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['email'] 

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin


# user activation by email 
class ActivationProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    key  = models.CharField(max_length=120)
    expired = models.BooleanField(default=False)  

    def save(self, *args, **kwargs):
        self.key = code_generator()
        super(ActivationProfile, self).save(*args, **kwargs)


def post_save_user_activatio_receiver(sender, instance, created, *args, **kwargs):
    if created: 
        print('activate email')
        url = "http://localhost:8000/account/activate/" + instance.key
        # send email wit hactice key 
    

post_save.connect(post_save_user_activatio_receiver, sender=ActivationProfile)


# user profile
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    city = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.user.username


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
            ActivationProfile.objects.create(user=instance)
        except:
            pass


post_save.connect(post_save_user_model_receiver,sender=settings.AUTH_USER_MODEL)