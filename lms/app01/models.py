from django.db import models

# Create your models here.


# 出版社类
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)


# 书籍的类
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)  # 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，


# 作者的类
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    # 一个作者可以对应多本书，一本书也可以有多个作者，多对多，在数据库中创建第三张表
    books = models.ManyToManyField(Book)


