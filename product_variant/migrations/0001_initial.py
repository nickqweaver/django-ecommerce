# Generated by Django 3.2.7 on 2021-11-04 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WheelProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(default='', max_length=150)),
                ('stock', models.IntegerField(default=0)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('size', models.CharField(choices=[('14x8', '14x8'), ('14x10', '14x10'), ('15x7', '15x7'), ('15x8', '15x8'), ('15x10', '15x10')], default='15x7', max_length=6)),
                ('bolt_pattern', models.CharField(choices=[('14x136', 'Rzr'), ('14x156', 'Can')], default='RZR', max_length=6)),
                ('product_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='product.wheelproductmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TireProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(default='', max_length=150)),
                ('stock', models.IntegerField(default=0)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('height', models.IntegerField(choices=[(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35)])),
                ('width', models.IntegerField(choices=[(8, 8), (9, 9), (10, 10)])),
                ('rim_circumference', models.IntegerField(choices=[(14, 14), (15, 15), (16, 16)])),
                ('product_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='product.tireproductmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
