from datetime import date
from django.db import models
from accounts.models import Users

from django.dispatch import receiver
import os

class Books(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.name

class Records(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(default=date.today())
    picture = models.FileField(upload_to='record_pictures')
    memo = models.CharField(max_length=255, blank=True)
    book = models.ForeignKey(
        Books, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'records'
    
    def __str__(self):
        return self.name


@receiver(models.signals.post_delete, sender=Records)
#recordが削除された場合に画像も削除
def delete_picture(sender, instance, **kwargs):
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)