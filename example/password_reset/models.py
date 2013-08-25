from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver

class Burn(models.Model):
    link = models.CharField(max_length=36, unique=True)
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return unicode(self.user)

    def reset(self):
        self.link = str(uuid4())

@receiver(post_save, sender=User)
def create_initial_link(sender, instance=None, created=False, **kwargs):
    if created:
        link = Burn.objects.create(user=instance)
        link.reset()
        while link.link in [x.link for x in Burn.objects.all()]:
            link.reset()
        link.save()
