# Generated by Django 4.0 on 2023-07-02 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_alter_client_contact_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client_contact',
            options={'verbose_name': 'Client_contact', 'verbose_name_plural': 'Client_contact'},
        ),
    ]