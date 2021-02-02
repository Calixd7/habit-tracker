# Generated by Django 3.1.5 on 2021-02-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210201_1029'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='record',
            name='unique_habit ',
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.UniqueConstraint(fields=('habit', 'date'), name='unique_habit'),
        ),
    ]
