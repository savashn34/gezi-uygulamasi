# Generated by Django 5.0.4 on 2024-04-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geziuygulamasi', '0025_remove_takimlar_baslangic_remove_takimlar_bitis_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takimlar',
            name='baslangic_ayi',
        ),
        migrations.RemoveField(
            model_name='takimlar',
            name='baslangic_gunu',
        ),
        migrations.RemoveField(
            model_name='takimlar',
            name='baslangic_yili',
        ),
        migrations.RemoveField(
            model_name='takimlar',
            name='bitis_ayi',
        ),
        migrations.RemoveField(
            model_name='takimlar',
            name='bitis_gunu',
        ),
        migrations.RemoveField(
            model_name='takimlar',
            name='bitis_yili',
        ),
        migrations.AddField(
            model_name='takimlar',
            name='baslangic',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='takimlar',
            name='bitis',
            field=models.DateTimeField(null=True),
        ),
    ]
