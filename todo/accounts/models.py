from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
    dob = models.DateField(null=True)
    
    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            UserProfileModel.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def update_user_profile(sender,instance,created,**kwargs):
        instance.userprofilemodel.save()

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    todo = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

