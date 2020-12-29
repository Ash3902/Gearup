# Generated by Django 3.0 on 2020-12-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
