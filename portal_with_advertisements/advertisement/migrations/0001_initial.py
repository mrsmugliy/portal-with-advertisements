# Generated by Django 3.2.2 on 2021-05-08 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of category')),
                ('ordering', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title of offer')),
                ('description', models.CharField(max_length=250, verbose_name='Description of offer')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price of offer')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date and time of creation of the offer')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.category', verbose_name='Offer category')),
            ],
        ),
    ]
