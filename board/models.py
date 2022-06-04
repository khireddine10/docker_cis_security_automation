from django.db import models

# Create your models here.
class host(models.Model):
    hostname = models.CharField(max_length=200, null=False)
    ip = models.CharField(max_length=200, null=False)
    user = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.hostname
    