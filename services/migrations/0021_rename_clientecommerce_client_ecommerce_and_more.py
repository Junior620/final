# Generated by Django 4.0 on 2023-07-02 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0020_clientecommerce'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClienteCommerce',
            new_name='Client_eCommerce',
        ),
        migrations.AlterModelOptions(
            name='client_ecommerce',
            options={'verbose_name': 'Client_eCommerce', 'verbose_name_plural': 'Client_eCommerce'},
        ),
    ]