# Generated by Django 3.2.6 on 2022-03-22 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0006_remove_blog_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]