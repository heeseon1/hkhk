# Generated by Django 3.2.20 on 2023-08-17 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_user_profileimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='warning',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
