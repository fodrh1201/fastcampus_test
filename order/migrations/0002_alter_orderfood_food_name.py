# Generated by Django 3.2.2 on 2022-01-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderfood',
            name='food_name',
            field=models.CharField(max_length=20),
        ),
    ]
