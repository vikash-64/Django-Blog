# Generated by Django 3.2.6 on 2022-03-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0004_remove_blog_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]