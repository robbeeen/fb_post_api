# Generated by Django 2.2.2 on 2023-03-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb_post', '0004_auto_20230221_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commented_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='reacted_by',
        ),
        migrations.AddField(
            model_name='comment',
            name='commented_by_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='posted_by_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='reaction',
            name='reacted_by_id',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
