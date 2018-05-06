from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    phone = models.IntegerField(default=0)
    city = models.CharField(max_length=100, default='')
    about = models.CharField(max_length=100, default='')
    photo = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)