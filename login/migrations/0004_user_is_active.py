# Generated by Django 3.0.2 on 2020-01-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200116_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
