# Generated by Django 4.0 on 2023-07-02 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_clientwordpress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientwordpress',
            old_name='Nom_c',
            new_name='Nom_client',
        ),
        migrations.RenameField(
            model_name='clientwordpress',
            old_name='Nom_e',
            new_name='Nom_entreprise',
        ),
    ]