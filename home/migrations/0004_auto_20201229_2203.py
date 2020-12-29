# Generated by Django 3.0 on 2020-12-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201229_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='name',
        ),
        migrations.AddField(
            model_name='blog',
            name='author_name',
            field=models.CharField(default='', help_text='maximum 30 words', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='heading',
            field=models.CharField(help_text='maximun, 200 words', max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]