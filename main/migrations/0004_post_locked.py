# Generated by Django 3.2.16 on 2023-03-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230203_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]
