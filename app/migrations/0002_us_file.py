# Generated by Django 2.0 on 2021-10-25 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='us_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(default='slogan', max_length=255)),
                ('o_file', models.FileField(default='.xls', max_length=255, upload_to='')),
            ],
        ),
    ]
