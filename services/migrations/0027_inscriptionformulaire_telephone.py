# Generated by Django 4.0 on 2023-07-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0026_remove_inscriptionformulaire_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscriptionformulaire',
            name='telephone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]