# Generated by Django 3.2.6 on 2022-03-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0002_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
