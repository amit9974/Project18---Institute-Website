# Generated by Django 4.1.2 on 2022-10-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_blogcategories_posts_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='img',
            field=models.ImageField(null=True, upload_to='media/post'),
        ),
    ]
