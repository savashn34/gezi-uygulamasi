# Generated by Django 5.0.4 on 2024-04-12 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geziuygulamasi', '0023_etkinlik_ayrintilari_yemek_yeri'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik_ayrintilari',
            name='ucus_alani',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geziuygulamasi.ucus_alanlari'),
        ),
    ]
