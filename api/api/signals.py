# Signal to create a client when a user is created

from django.contrib.auth.models import User
from .models import Client
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    print('Created:',created)
    if created:
        print(type(Client))
        print(instance)
        print(instance.username)
        Client.objects.create(user=instance, name=instance.username)
        print('Client created!')