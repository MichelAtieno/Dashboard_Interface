# Generated by Django 3.2.4 on 2021-07-02 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0002_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
    ]