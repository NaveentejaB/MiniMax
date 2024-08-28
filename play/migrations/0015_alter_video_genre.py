# Generated by Django 4.1.2 on 2023-05-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0014_video_genre_video_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='genre',
            field=models.CharField(blank=True, choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Romance', 'Romance'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Science Fiction', 'Science Fiction'), ('Thriller', 'Thriller'), ('Mystery', 'Mystery'), ('Historical', 'Historical'), ('Historical Fiction', 'Historical Fiction'), ('Philosophical', 'Philosophical'), ('Political', 'Political')], max_length=100, null=True),
        ),
    ]
