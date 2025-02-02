from django.db import models
from django.contrib.auth.models import User
from adult.models import Adultmodel

# Create your models here.
GENDER=(('secondary','-'),('danger','♀'),('info','♂'))
class Childmodel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='child',null=True)
    number = models.IntegerField('管理番号')
    name = models.CharField('名前',max_length=100)
    gender = models.CharField(
        '性別',
        max_length=50,
        choices=GENDER,
    )
    gener=models.CharField('累代',max_length=100,null=True, blank=True)
    size_ad = models.CharField('種親サイズ',max_length=100,null=True, blank=True)
    ad_date = models.DateField('種親羽化日',null=True, blank=True)
    date = models.DateField('割り出し日',null=True, blank=True)
    date_1 = models.DateField('1本目',null=True, blank=True)
    date_2 = models.DateField('2本目',null=True, blank=True)
    date_3 = models.DateField('3本目',null=True, blank=True)
    date_4 = models.DateField('4本目',null=True, blank=True)
    date_5 = models.DateField('羽化日',null=True, blank=True)
    weight_1=models.FloatField('1回目の体重',null=True, blank=True)
    weight_2=models.FloatField('2回目の体重',null=True, blank=True)
    weight_3=models.FloatField('3回目の体重',null=True, blank=True)
    weight_4=models.FloatField('4回目の体重',null=True, blank=True)
    memo = models.TextField('メモ',null=True, blank=True)
    image = models.ImageField(upload_to='media',null=True,blank=True)
    def __str__(self):
        return f"{self.date}{self.name}{self.number}"
    