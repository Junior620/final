# Generated by Django 4.0 on 2023-07-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_inscriptionformulaire_choix'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscriptionformulaire',
            name='date_naissance',
            field=models.DateField(null=True),
        ),
    ]