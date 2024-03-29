# Generated by Django 3.0.5 on 2020-11-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('presion', models.FloatField()),
                ('humedad', models.FloatField()),
                ('temperatura', models.FloatField()),
                ('co2_ppm', models.FloatField()),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
    ]
