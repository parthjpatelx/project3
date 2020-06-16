# Generated by Django 3.0.7 on 2020-06-16 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200615_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.FloatField(max_length=4)),
            ],
        ),
        migrations.AlterField(
            model_name='platter',
            name='price',
            field=models.FloatField(max_length=4),
        ),
    ]
