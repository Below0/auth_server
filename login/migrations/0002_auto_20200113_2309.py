# Generated by Django 3.0.2 on 2020-01-13 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='pw',
            field=models.CharField(max_length=65),
        ),
    ]
