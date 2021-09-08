# Generated by Django 3.1.4 on 2021-09-08 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models
import reprohack_hub.models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack_hub', '0014_auto_20210908_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=markdownx.models.MarkdownxField(default=reprohack_hub.models.get_default_description, verbose_name='Event Description. We provide a markdown template but feel free to customise'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='submitter',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='operating_system',
            field=models.CharField(choices=[('linux', 'Linux/FreeBSD or other Open Source Operating system'), ('macOS', 'Apple Operating System (macOSX)'), ('windows', 'Windows Operating System')], max_length=7, verbose_name='Which type of operating system were you working in?'),
        ),
    ]
