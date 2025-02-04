from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class PaymentCategory(models.Model):
    """支出カテゴリ"""
    name = models.CharField('カテゴリ名', max_length=32)
    

    def __str__(self):
        return self.name


class Payment(models.Model):
    """支出"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('日付')
    amount = models.IntegerField('金額')
    category = models.ForeignKey(PaymentCategory, on_delete=models.PROTECT, verbose_name='カテゴリ')
    description = models.TextField('摘要', null=True, blank=True)


class IncomeCategory(models.Model):
    """収入カテゴリ"""
    name = models.CharField('カテゴリ名', max_length=32)

    def __str__(self):
        return self.name


class Income(models.Model):
    """収入"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('日付')
    amount = models.IntegerField('金額')
    category = models.ForeignKey(IncomeCategory, on_delete=models.PROTECT, verbose_name='カテゴリ')
    description = models.TextField('摘要', null=True, blank=True)



