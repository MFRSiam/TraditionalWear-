# Generated by Django 4.0.4 on 2022-05-01 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_products_productimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='orders',
            name='ProductID',
            field=models.ForeignKey(db_constraint=False, default=0, on_delete=django.db.models.deletion.CASCADE, to='store.products'),
        ),
    ]
