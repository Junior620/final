# Generated by Django 4.0 on 2023-07-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_alter_inscriptionformulaire_choix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscriptionformulaire',
            name='choix',
            field=models.BooleanField(),
        ),
    ]