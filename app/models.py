from django.db import models
from django.contrib.auth.models import User
# Create your models here.

import datetime
from django.db import models
from django.utils import timezone

PRIORITY=(('danger','高'),('info','中'),('success','低'))
class Schedule(models.Model):
    """スケジュール"""
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='calendar',null=True)#追加
    summary = models.CharField('概要', max_length=50)
    description = models.TextField('詳細説明', blank=True)
    start_time = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('終了時間', default=datetime.time(7, 0, 0))
    date = models.DateField('日付')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    priority=models.CharField(
        '優先度',
        max_length=50,
        choices=PRIORITY,

    )

    def __str__(self):
        return self.summary