# Generated by Django 3.0 on 2020-12-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201229_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='meta_description',
            field=models.TextField(default='', help_text='Minimum 100 Words'),
            preserve_default=False,
        ),
    ]
