# Generated by Django 2.2.2 on 2023-02-13 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb_post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 13, 14, 37, 46, 815525)),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='reacted_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 13, 14, 37, 46, 816024)),
        ),
    ]
