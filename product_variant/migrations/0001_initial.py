# Generated by Django 3.2.6 on 2021-08-31 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0010_wheelproductmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='WheelProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XS', '14x8'), ('S', '14x10'), ('M', '15x7'), ('L', '15x8'), ('XL', '15x10')], default='M', max_length=2)),
                ('bolt_pattern', models.CharField(choices=[('RZR', '14x136'), ('CAN', '14x156')], default='RZR', max_length=3)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_code', models.CharField(max_length=150)),
                ('product_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='product.wheelproductmodel')),
            ],
        ),
    ]
