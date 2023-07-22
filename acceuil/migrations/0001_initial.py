# Generated by Django 4.0 on 2023-07-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcceuilContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('telephone', models.FloatField(max_length=50)),
                ('decryption', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'AcceilContact',
                'verbose_name_plural': 'AcceuilContact',
            },
        ),
    ]
