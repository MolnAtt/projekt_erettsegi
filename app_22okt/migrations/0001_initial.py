# Generated by Django 4.2 on 2023-04-18 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Festo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=255)),
                ('szuletett', models.IntegerField()),
                ('meghalt', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Festő',
                'verbose_name_plural': 'Festők',
            },
        ),
        migrations.CreateModel(
            name='Kep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cim', models.CharField(max_length=255)),
                ('keszult', models.IntegerField()),
                ('anyag', models.CharField(max_length=255)),
                ('technika', models.CharField(max_length=255)),
                ('szeles', models.FloatField()),
                ('magas', models.FloatField()),
                ('festo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_22okt.festo')),
            ],
            options={
                'verbose_name': 'Kép',
                'verbose_name_plural': 'Képek',
            },
        ),
    ]