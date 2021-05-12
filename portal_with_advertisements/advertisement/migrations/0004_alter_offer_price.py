# Generated by Django 3.2.2 on 2021-05-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_auto_20210508_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price of offer'),
        ),
    ]