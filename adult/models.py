from django.db import models
from django.contrib.auth.models import User

GENDER=(('danger','♀'),('info','♂'))
class Adultmodel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='adult',null=True)#追加
    name = models.CharField('名前',max_length=100)
    gender = models.CharField(
        '性別',
        max_length=50,
        choices=GENDER,
    )
    gener=models.CharField('累代',max_length=100)
    size = models.CharField('サイズ',max_length=100)
    date = models.DateField('羽化日')
    memo = models.TextField('メモ')
    image = models.ImageField(upload_to='media',null=True,blank=True)
    def __str__(self):
        return f"{self.name}{self.date}{self.size}"

class contact(models.Model):
    title= models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

