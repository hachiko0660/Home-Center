# Generated by Django 5.0.1 on 2024-01-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0013_ofrmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofrmodel',
            name='descript',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ofrmodel',
            name='prodid1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]