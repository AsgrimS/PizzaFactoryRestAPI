# Generated by Django 3.1.6 on 2021-02-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210214_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzas',
            name='name',
            field=models.CharField(default='example', max_length=30),
            preserve_default=False,
        ),
    ]
