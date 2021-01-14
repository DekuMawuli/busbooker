from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from zope.interface import named


class CustomUser(AbstractUser):
    ROLE = [
        (1, "Regular"),
        (2, "Administrator"),
    ]
    phone = models.CharField(max_length=10)
    role = models.PositiveSmallIntegerField(choices=ROLE, default=1)


@receiver(signal=post_save, sender=CustomUser)
def user_created(sender, instance, created, **kwargs):
    reg, created = Group.objects.get_or_create(name="Regular")
    admin, created = Group.objects.get_or_create(name="Administrator")
    if created:
        if instance.role == 1:
            print("Regular")
            reg.user_set.add(instance)
        else:
            print("Admin")
            admin.user_set.add(instance)
    else:
        if instance.role == 1:
            admin.user_set.remove(instance)
            reg.user_set.add(instance)
        else:
            reg.user_set.remove(instance)
            admin.user_set.add(instance)
