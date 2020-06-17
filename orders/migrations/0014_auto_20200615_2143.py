# Generated by Django 3.0.7 on 2020-06-16 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20200615_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasta',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Pasta_type'),
        ),
        migrations.AlterField(
            model_name='sub',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Sub_type'),
        ),
    ]