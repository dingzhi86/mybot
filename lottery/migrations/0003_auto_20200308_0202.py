# Generated by Django 3.0.1 on 2020-03-07 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0002_auto_20200308_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='rarity',
            field=models.ForeignKey(db_column='', on_delete=django.db.models.deletion.PROTECT, to='lottery.Rarity', verbose_name='稀有度'),
        ),
    ]
