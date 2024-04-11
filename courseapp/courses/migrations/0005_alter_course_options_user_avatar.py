# Generated by Django 5.0.4 on 2024-04-11 16:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_tag_category_icon_lesson_comment_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
    ]
