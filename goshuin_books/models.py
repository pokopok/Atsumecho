from datetime import date
from django.db import models
from accounts.models import Users

from django.dispatch import receiver
import os

class GoshuinBooks(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'goshuin_books'

    def __str__(self):
        return self.name

class Goshuins(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(default=date.today())
    picture = models.FileField(upload_to='goshuin_pictures')
    memo = models.CharField(max_length=255, blank=True)
    goshuin_book = models.ForeignKey(
        GoshuinBooks, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'goshuins'
    
    def __str__(self):
        return self.name


@receiver(models.signals.post_delete, sender=Goshuins)
#Goshuinsが削除された場合に画像も削除
def delete_picture(sender, instance, **kwargs):
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)