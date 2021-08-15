# Generated by Django 3.2.6 on 2021-08-15 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('option', '0002_auto_20210815_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoption',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='optionitem',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='option.option'),
        ),
    ]
