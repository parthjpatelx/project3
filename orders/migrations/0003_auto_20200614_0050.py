# Generated by Django 2.0.3 on 2020-06-14 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200614_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='type',
            field=models.CharField(max_length=64),
        ),
    ]