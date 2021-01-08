# Generated by Django 2.2.13 on 2020-12-29 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_blog_meta_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_section_last',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('sub_heading', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='home')),
            ],
        ),
        migrations.CreateModel(
            name='Home_setion_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('sub_heading', models.CharField(max_length=100)),
                ('background_image', models.FileField(blank=True, null=True, upload_to='home/')),
                ('heading2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Home_setion_2_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='icon/')),
                ('heading', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Manage_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=20)),
                ('service_price_text', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Our_client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Why_Choose_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('sub_heading', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Why_Choose_us_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=90)),
                ('us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Why_Choose_us')),
            ],
        ),
        migrations.CreateModel(
            name='Service_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=60)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Manage_service')),
            ],
        ),
        migrations.CreateModel(
            name='Home_section_last_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=90)),
                ('last_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Home_section_last')),
            ],
        ),
        migrations.CreateModel(
            name='Client_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=90)),
                ('client_image', models.FileField(upload_to='client/')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Our_client')),
            ],
        ),
    ]