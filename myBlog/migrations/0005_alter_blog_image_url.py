# Generated by Django 3.2.6 on 2022-03-26 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0004_rename_imgagr_url_blog_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Image_URL',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
