# Generated by Django 4.2.1 on 2024-01-15 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_alter_productmodel1_descript'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel1',
            name='descript',
            field=models.CharField(max_length=500),
        ),
    ]
