# Generated by Django 2.2.6 on 2019-10-27 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0008_remove_content_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title_picture',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]