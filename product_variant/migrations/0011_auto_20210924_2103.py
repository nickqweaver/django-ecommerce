# Generated by Django 3.2.7 on 2021-09-24 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_variant', '0010_remove_wheelproductvariant_finish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wheelproductvariant',
            name='bolt_pattern',
            field=models.CharField(choices=[('14x136', 'Rzr'), ('14x156', 'Can')], default='RZR', max_length=6, verbose_name='bolt pattern'),
        ),
        migrations.AlterField(
            model_name='wheelproductvariant',
            name='size',
            field=models.CharField(choices=[('14x8', '14x8'), ('14x10', '14x10'), ('15x7', '15x7'), ('15x8', '15x8'), ('15x10', '15x10')], default='15x7', max_length=6, verbose_name='size'),
        ),
    ]