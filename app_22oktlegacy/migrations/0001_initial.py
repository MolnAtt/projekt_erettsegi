# Generated by Django 4.2 on 2023-04-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kerulet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('szam', models.CharField(max_length=50)),
                ('nev', models.CharField(blank=True, max_length=100, null=True)),
                ('lakossag', models.IntegerField()),
                ('terulet', models.FloatField()),
            ],
            options={
                'verbose_name': 'Kerület',
                'verbose_name_plural': 'Kerületek',
            },
        ),
        migrations.CreateModel(
            name='Varosresz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('azon', models.IntegerField()),
                ('nev', models.CharField(blank=True, max_length=100, null=True)),
                ('lakossag', models.IntegerField(blank=True, null=True)),
                ('kerulet', models.ManyToManyField(to='app_22oktlegacy.kerulet')),
            ],
            options={
                'verbose_name': 'Városrész',
                'verbose_name_plural': 'Városrészek',
            },
        ),
    ]
