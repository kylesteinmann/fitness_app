# Generated by Django 4.2.7 on 2023-11-10 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='sets',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
