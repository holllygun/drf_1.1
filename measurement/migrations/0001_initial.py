# Generated by Django 4.2.7 on 2024-01-04 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Температура при измерении')),
                ('datetime', models.DateField(auto_now_add=True, verbose_name='Дата и время измерения')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='measurement.sensor')),
            ],
        ),
    ]
