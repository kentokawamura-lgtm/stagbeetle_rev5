# Generated by Django 5.1.5 on 2025-02-05 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adult', '0006_alter_adultmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adultmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
