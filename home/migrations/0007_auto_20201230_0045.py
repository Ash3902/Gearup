# Generated by Django 2.2.13 on 2020-12-29 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_client_detail_home_section_last_home_section_last_text_home_setion_1_home_setion_2_card_manage_servi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_setion_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='home_setion_2_card',
            old_name='heading',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='home_setion_1',
            name='heading2',
        ),
        migrations.AddField(
            model_name='home_setion_2_card',
            name='section_2',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.Home_setion_2'),
            preserve_default=False,
        ),
    ]