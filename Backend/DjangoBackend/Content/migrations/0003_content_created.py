# Generated by Django 2.2.6 on 2019-10-26 21:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0002_article_event_image_media_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
