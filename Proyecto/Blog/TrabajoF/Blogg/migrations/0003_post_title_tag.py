# Generated by Django 4.1.4 on 2022-12-27 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogg', '0002_rename_autho_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blog Universitario', max_length=200),
        ),
    ]