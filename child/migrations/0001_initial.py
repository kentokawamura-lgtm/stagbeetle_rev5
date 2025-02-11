# Generated by Django 5.1.5 on 2025-02-02 03:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Childmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='管理番号')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('gender', models.CharField(choices=[('secondary', '-'), ('danger', '♀'), ('info', '♂')], max_length=50, verbose_name='性別')),
                ('gener', models.CharField(blank=True, max_length=100, null=True, verbose_name='累代')),
                ('size_ad', models.CharField(blank=True, max_length=100, null=True, verbose_name='種親サイズ')),
                ('ad_date', models.DateField(blank=True, null=True, verbose_name='種親羽化日')),
                ('date', models.DateField(blank=True, null=True, verbose_name='割り出し日')),
                ('date_1', models.DateField(blank=True, null=True, verbose_name='1本目')),
                ('date_2', models.DateField(blank=True, null=True, verbose_name='2本目')),
                ('date_3', models.DateField(blank=True, null=True, verbose_name='3本目')),
                ('date_4', models.DateField(blank=True, null=True, verbose_name='4本目')),
                ('date_5', models.DateField(blank=True, null=True, verbose_name='羽化日')),
                ('weight_1', models.FloatField(blank=True, null=True, verbose_name='1回目の体重')),
                ('weight_2', models.FloatField(blank=True, null=True, verbose_name='2回目の体重')),
                ('weight_3', models.FloatField(blank=True, null=True, verbose_name='3回目の体重')),
                ('weight_4', models.FloatField(blank=True, null=True, verbose_name='4回目の体重')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='メモ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
