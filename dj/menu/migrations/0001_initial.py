# Generated by Django 3.2.15 on 2022-09-08 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('descripcion', models.CharField(max_length=128)),
                ('img_url', models.CharField(max_length=256)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.categoria')),
            ],
        ),
    ]
