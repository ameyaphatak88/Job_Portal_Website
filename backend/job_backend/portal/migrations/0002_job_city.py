# Generated by Django 3.0.7 on 2020-07-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='city',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
    ]