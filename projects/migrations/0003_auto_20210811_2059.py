# Generated by Django 3.2.6 on 2021-08-11 12:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projects'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': '项目表'},
        ),
        migrations.RemoveField(
            model_name='projects',
            name='descripe',
        ),
        migrations.AddField(
            model_name='projects',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True, default='描述语句', help_text='项目描述', null=True, verbose_name='项目描述'),
        ),
        migrations.AddField(
            model_name='projects',
            name='update_time',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='id',
            field=models.IntegerField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='is_execute',
            field=models.BooleanField(default=True, help_text='是否启动项目', verbose_name='是否启动项目'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='leader',
            field=models.CharField(help_text='项目负责人', max_length=20, verbose_name='项目负责人'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.CharField(help_text='项目名称', max_length=50, unique=True, verbose_name='项目名称'),
        ),
        migrations.AlterModelTable(
            name='projects',
            table='tb_projects',
        ),
    ]