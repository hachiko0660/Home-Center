# Generated by Django 5.0.1 on 2024-01-25 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0015_wishmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('comments', models.CharField(max_length=500)),
            ],
        ),
    ]
