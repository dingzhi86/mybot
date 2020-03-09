# Generated by Django 3.0.1 on 2020-03-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0003_auto_20200308_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.FloatField(default=1, verbose_name='部件权重'),
        ),
        migrations.AlterField(
            model_name='rarity',
            name='weight',
            field=models.FloatField(verbose_name='稀有度权重'),
        ),
    ]