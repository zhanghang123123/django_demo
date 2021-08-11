from django.db import models


# Create your models here.
class Interfaces(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id主键', help_text='id主键')
    name = models.CharField(verbose_name='接口名称', help_text='接口名称', max_length=20)
    tester = models.CharField(verbose_name='接口测试人员', help_text='接口测试人员', max_length=20)

    projects = models.ForeignKey('projects.Projects', on_delete=models.CASCADE)

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

    # 定制该表  内部类 给当前模型类 添加元素信息
    class Meta:
        db_table = 'tb_interfaces'
        verbose_name = '接口表'
        verbose_name_plural = '接口表'
        ordering = ['id', 'name']
