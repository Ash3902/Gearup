# Generated by Django 3.0 on 2020-12-29 16:24

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='add_to_feature_post',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='publish_now',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
