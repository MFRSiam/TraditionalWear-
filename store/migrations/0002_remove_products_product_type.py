# Generated by Django 4.0.4 on 2022-04-22 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Product_Type',
        ),
    ]