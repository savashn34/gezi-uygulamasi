# Generated by Django 5.0.4 on 2024-04-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geziuygulamasi', '0026_remove_takimlar_baslangic_ayi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takimlar',
            name='baslangic',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='takimlar',
            name='bitis',
            field=models.DateTimeField(),
        ),
    ]