# Generated by Django 3.2.6 on 2021-08-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('leader', models.CharField(max_length=20)),
                ('is_execute', models.BooleanField()),
                ('descripe', models.TextField()),
            ],
        ),
    ]