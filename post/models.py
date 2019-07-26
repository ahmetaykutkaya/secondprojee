from django.db import models
from django.urls import reverse 

# Create your models here.
from django.utils import timezone


class GunType(models.Model):
    title = models.CharField(max_length=200 )
    code = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.title


class GunBrand(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.title


class PersonelClass(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)
    rank_order = models.IntegerField(default=0)
    logo = models.ImageField(upload_to="images/rank")

    def __str__(self):
        return self.title


class Rank(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)
    rank_order = models.IntegerField(default=0)
    logo = models.ImageField(upload_to="images/rank")
    
    def __str__(self):
        return self.title
    
    
class Personel(models.Model):
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)
    personel_class = models.ForeignKey(PersonelClass, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    image = models.ImageField(upload_to="images/personel")

    def __str__(self):
        return self.name + " " + self.surname
    
    
class Gun(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)
    type = models.ForeignKey(GunType, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(GunBrand, on_delete=models.DO_NOTHING)
    serial = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="images/personel")

    def __str__(self):
        return self.title + "(" + self.code + ")"
    

class GunStorage(models.Model):
    personel = models.ForeignKey(Personel, on_delete=models.DO_NOTHING)
    gun = models.ForeignKey(Gun, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.personel.name + " " + self.personel.middlename + " " + self.personel.surname + " - " + self.gun.title
    