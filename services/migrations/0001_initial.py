# Generated by Django 4.0 on 2023-07-01 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription_formulaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('date_de_naissance', models.DateField()),
                ('lieu_de_naissance', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('telephone', models.FloatField(max_length=50)),
                ('ville', models.CharField(max_length=30)),
                ('profession', models.CharField(max_length=50)),
            ],
        ),
    ]