# Generated by Django 4.1 on 2022-08-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hava_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hava',
            name='sehir',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]