import string

from django.db import models
import random
import string

# Create your models here.
class Url(models.Model):
    original_url = models.URLField(max_length=999)
    short_url = models.CharField(max_length=6, unique=True)
    clicks = models.IntegerField(default=0)

    def save(self,*args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
            super.save(*args, **kwargs)


    def generate_short_url(self):
        return ''.join(random.choice(string.ascii_letters + string.digits, k=6))

    def __str__(self):
        return f'{self.short_url}-{self.original_url}'

