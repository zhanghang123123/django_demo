from django.db import models
from utils.basemodel import BaseModel


# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Projects(BaseModel):
    # unique = True 指定当前字段为唯一约束
    # null = True 指定数据库中当前字段可以值为空 null, ORM默认是NOT NULL 非空
    # id = models.IntegerField(primary_key=True, verbose_name='id主键', help_text='id主键')
    name = models.CharField(max_length=50, unique=True, verbose_name='项目名称', help_text='项目名称')
    leader = models.CharField(max_length=20, verbose_name='项目负责人', help_text='项目负责人')
    # default= True 为当前字段指定默认值，指定默认值以后，前端创建数据时如果不指定该字段，那么将自动把default值作为当前字段值
    is_execute = models.BooleanField(verbose_name='是否启动项目', help_text='是否启动项目', default=True)
    # blank=True 指定前端在创建数据时可以不用给该字段传值，默认前端创建时是需要必须传递该字段值
    description = models.TextField(verbose_name='项目描述', help_text='项目描述', null=True, blank=True, default="描述语句")

    # 可以为DateTimeField、DateField字段添加auto_now_add、auto_now参数
    # >> auto_now_add=True指定在创建该记录时，会自动将当前字段创建时间作为该字段的值，后续不会变更
    # >> auto_now=True指定在创建该记录时，会自动将当前字段更新时间作为该字段的值，后续只要更新了该记录，都会自动修改
    # >> auto_now_add和auto_now不能同时指定
    # create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    # update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

    # 定制该表  内部类 给当前模型类 添加元素信息
    class Meta:
        db_table = 'tb_projects'
        verbose_name = '项目表'
        verbose_name_plural = '项目表'
        ordering = ['id', 'name']
