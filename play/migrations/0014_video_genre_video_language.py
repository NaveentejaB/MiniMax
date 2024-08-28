# Generated by Django 4.1.2 on 2023-05-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0013_alter_video_subtitle_alter_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='genre',
            field=models.CharField(blank=True, choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Romance', 'Romance'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Science Fiction', 'Science Fiction'), ('Thriller', 'Thriller'), ('Mystery', 'Mystery'), ('Historical', 'Historical'), ('Historical Fiction', 'Historical Fiction'), ('Philosophical', 'Philosophical'), ('Political', 'Political')], default='Action', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Marathi', 'Marathi'), ('Kannada', 'Kannada'), ('Tamil', 'Tamil'), ('Telugu', 'Telugu'), ('Malayalam', 'Malayalam'), ('Bengali', 'Bengali'), ('Punjabi', 'Punjabi'), ('Gujarati', 'Gujarati')], default='English', max_length=100, null=True),
        ),
    ]
