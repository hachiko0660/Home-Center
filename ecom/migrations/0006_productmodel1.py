# Generated by Django 4.2.1 on 2024-01-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_alter_productmodel_descrpt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='productmodel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('img', models.FileField(upload_to='ecom/static')),
                ('price', models.IntegerField()),
                ('prodid1', models.IntegerField()),
                ('descript', models.CharField(max_length=250)),
            ],
        ),
    ]
