# Generated by Django 3.0.7 on 2020-06-18 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200615_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='orders.Size'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='orders.Pizza_style'),
        ),
    ]
