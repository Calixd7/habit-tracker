# Generated by Django 3.1.5 on 2021-01-21 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('target', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='core.habit')),
            ],
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.UniqueConstraint(fields=('habit', 'date'), name='unique_habit '),
        ),
    ]
