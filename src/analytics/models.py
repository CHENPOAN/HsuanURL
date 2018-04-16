from django.db import models

# Create your models here.
from shortener.models import HsuanURL


class ClickEventManager(models.Manager):
    def create_event(self, hsuanInstance):
        if isinstance(hsuanInstance, HsuanURL):
            obj, created = self.get_or_create(hsuan_url=hsuanInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    hsuan_url   = models.OneToOneField(HsuanURL)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return str(self.hsuan_url)