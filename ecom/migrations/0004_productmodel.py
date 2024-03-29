# Generated by Django 4.2.1 on 2024-01-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_remove_regimodel_cpsw'),
    ]

    operations = [
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodname', models.CharField(max_length=20)),
                ('prodid', models.CharField(max_length=10)),
                ('prodprc', models.IntegerField()),
                ('descrpt', models.CharField(max_length=50)),
                ('proimg', models.FileField(upload_to='ecom/static')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
