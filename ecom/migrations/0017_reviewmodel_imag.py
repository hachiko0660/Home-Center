# Generated by Django 5.0.1 on 2024-01-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0016_reviewmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='imag',
            field=models.FileField(default=1, upload_to='ecom/static'),
            preserve_default=False,
        ),
    ]