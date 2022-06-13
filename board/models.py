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


class check(models.Model):
    checknumber = models.IntegerField()
    checkId = models.CharField(max_length=50, null=False)
    checkDescription = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.checkId


class correction(models.Model):
    checknumber = models.IntegerField()
    checklist = models.CharField(max_length=200, null=False)
