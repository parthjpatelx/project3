# Generated by Django 2.0.3 on 2020-06-15 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200615_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizes',
            name='size',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
