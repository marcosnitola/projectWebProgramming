# Generated by Django 3.2.15 on 2022-09-10 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_platillo_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platillo',
            name='precio',
            field=models.PositiveIntegerField(),
        ),
    ]