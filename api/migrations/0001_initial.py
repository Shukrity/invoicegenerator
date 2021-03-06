# Generated by Django 4.0 on 2021-12-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(max_length=200)),
                ('clientEmail', models.EmailField(max_length=254)),
                ('clientAddress', models.TextField()),
                ('clientGSTNum', models.CharField(max_length=50)),
                ('billerName', models.CharField(max_length=200)),
                ('billerEmail', models.EmailField(max_length=254)),
                ('billerAddress', models.TextField()),
                ('billerGSTNum', models.CharField(max_length=50)),
                ('servicesDetails', models.JSONField()),
                ('taxRate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bankAccDetails', models.TextField()),
            ],
        ),
    ]
