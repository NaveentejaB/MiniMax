# Generated by Django 4.1.2 on 2023-05-20 10:42

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0003_alter_channel_channel_id_alter_video_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='channel_id',
            field=models.UUIDField(default=shortuuid.main.ShortUUID.uuid, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.UUIDField(default=shortuuid.main.ShortUUID.uuid, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
