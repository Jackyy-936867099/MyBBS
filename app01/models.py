from django.db import models

# Create your models here.
"""
先写普通字段
之后再写外键字段
"""
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    phone = models.BigIntegerField(verbose_name='手机号',null=True,blank=True)
    avatar = models.FileField(upload_to='avatar/',default='avatar/default.png')
    creat_time = models.DateField(auto_now_add=True)

    blog = models.OneToOneField(to='Blog',null=True)

    class Meta:
        verbose_name_plural = '用户表' # 修改admin后台管理默认的表名

    def __str__(self):
        return self.username


class Blog(models.Model):
    site_name = models.CharField(verbose_name='站点名称',max_length=32)
    site_title = models.CharField(verbose_name='站点标题',max_length=32)
    site_theme = models.CharField(verbose_name='站点样式',max_length=32)  # 存css/js文件

    class Meta:
        verbose_name_plural = '个人站点'

    def __str__(self):
        return self.site_name

class Category(models.Model):
    name = models.CharField(verbose_name='文章分类',max_length=32)
    blog = models.ForeignKey(to='Blog',null=True)

    class Meta:
        verbose_name_plural = '文章分类'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(verbose_name='标签分类', max_length=32)
    blog = models.ForeignKey(to='Blog',null=True)

    class Meta:
        verbose_name_plural = '文章标签'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(verbose_name='文章标题',max_length=64)
    desc = models.CharField(verbose_name='文章简介',max_length=255)
    content = models.TextField(verbose_name='文章内容')
    creat_time = models.DateField(auto_now_add=True)
    up_num = models.BigIntegerField(verbose_name='点赞数',default=0)
    down_num = models.BigIntegerField(verbose_name='点踩数',default=0)
    comment_num = models.BigIntegerField(verbose_name='点踩数',default=0)

    ##外键字段
    blog = models.ForeignKey(to='Blog',null=True)
    category = models.ForeignKey(to='Category',null=True)

    tags = models.ManyToManyField(to='Tag',
                                  through='Article2Tag',
                                  through_fields=('article','tag')
                                  )
    class Meta:
        verbose_name_plural = '文章表'

    def __str__(self):
        return self.title

class Article2Tag(models.Model):
    article = models.ForeignKey(to='Article')
    tag = models.ForeignKey(to='Tag')


class UpAndDown(models.Model):
    user = models.ForeignKey(to='UserInfo')
    article = models.ForeignKey(to='Article')
    is_up = models.BooleanField()

    class Meta:
        verbose_name_plural = '点赞点踩表'




class Comment(models.Model):
    user = models.ForeignKey(to='UserInfo')
    article = models.ForeignKey(to='Article')
    content = models.CharField(verbose_name='评论内容',max_length=255)
    parent = models.ForeignKey(to='self',null=True)
    comment_time = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '评论表'

