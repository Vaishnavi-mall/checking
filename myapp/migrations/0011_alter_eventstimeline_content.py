# Generated by Django 4.0.2 on 2022-04-21 19:17

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_eventstimeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventstimeline',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
