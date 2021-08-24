# Generated by Django 3.2.6 on 2021-08-24 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_thumbnail'),
        ('option', '0003_productoption_option_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductBrandOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_option', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='option.brandoption')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
