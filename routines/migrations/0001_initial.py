# Generated by Django 4.2.7 on 2023-11-15 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercises', '0006_exercise_incremental_weight_alter_exercise_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('exercises', models.ManyToManyField(blank=True, to='exercises.exercise')),
            ],
        ),
    ]