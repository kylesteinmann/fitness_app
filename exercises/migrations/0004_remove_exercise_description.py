# Generated by Django 4.2.7 on 2023-11-10 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_alter_exercise_sets_alter_exercise_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='description',
        ),
    ]
