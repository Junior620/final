# Generated by Django 4.0 on 2023-07-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_inscriptionformulaire_choix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscriptionformulaire',
            name='choix',
            field=models.BooleanField(default=True),
        ),
    ]
