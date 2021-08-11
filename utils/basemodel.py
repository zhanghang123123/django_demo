from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """
    主要意义是将不同ORM模型中的公共字段提取出来，用于被子模型类继承
    """
    id = models.IntegerField(primary_key=True, verbose_name='id主键', help_text='id主键')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

    class Meta:
        # abstract = True 告诉ORM框架，定义的这个模型类（表）是抽象类，在执行迁移脚本时，不用生成迁移文件，也不会生成迁移脚本。
        # 它的意义仅仅在于被其他模型类继承
        abstract = True
