# Generated by Django 3.1.4 on 2021-08-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack_hub', '0009_auto_20210719_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_initial_upload',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='paper',
            name='is_initial_upload',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='is_initial_upload',
            field=models.BooleanField(default=False),
        ),
    ]
