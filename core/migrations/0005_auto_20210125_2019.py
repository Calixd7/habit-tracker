# Generated by Django 3.1.5 on 2021-01-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_habit_noun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='noun',
            field=models.CharField(max_length=255),
        ),
    ]
