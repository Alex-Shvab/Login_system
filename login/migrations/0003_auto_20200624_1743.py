# Generated by Django 3.0.3 on 2020-06-24 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200624_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='co_worker',
            field=models.BooleanField(default=False),
        ),
    ]
