# Generated by Django 3.1.6 on 2021-02-14 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_crust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzas',
            name='crust',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.crust'),
        ),
    ]
