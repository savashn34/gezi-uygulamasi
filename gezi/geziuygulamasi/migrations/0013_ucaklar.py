# Generated by Django 5.0.4 on 2024-04-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geziuygulamasi', '0012_remove_etkinlikler_etkinlik_saati_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ucaklar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ucak', models.CharField(max_length=50)),
            ],
        ),
    ]
