# Generated by Django 4.0.2 on 2022-03-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_techfest_fest_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_image',
            field=models.ImageField(null=True, upload_to='event/images'),
        ),
        migrations.AddField(
            model_name='events',
            name='event_video',
            field=models.FileField(null=True, upload_to='event/videos'),
        ),
    ]
