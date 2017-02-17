# coding=utf-8
from django.db import models
from django.utils.datetime_safe import datetime


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=20, default='部门的名字')
    introduction = models.TextField(default='这是简介')

    def __unicode__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=20, default='组员名字')
    grade = models.CharField(max_length=20, default='')  # 大几
    rank = models.CharField(max_length=20, default='')
    introduction = models.TextField()
    image = models.ImageField(upload_to='staff')
    department = models.ForeignKey(Department)
    chef_flag = models.BooleanField(default=False)  # 是否是部长

    def __unicode__(self):
        return self.name


class X_news(models.Model):
    '''校学生会的新闻'''
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='xnews')
    video = models.CharField(max_length=200, blank=True)
    exc_editor = models.CharField(max_length=20, default='本新闻执行编辑')
    duty_editor = models.CharField(max_length=20, default='本新闻责任编辑')
    view_num = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=datetime.now())
    department = models.ForeignKey(Department)

    def __unicode__(self):
        return self.title


class X_activity(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='activity')
    video = models.CharField(max_length=200, blank=True)
    sponsor = models.CharField(max_length=20)
    datetime = models.DateTimeField(default=datetime.now())
    department = models.ForeignKey(Department)

    def __unicode__(self):
        return self.department.name + "的" + self.name + "活动"


########################################################################
########################################################################

class School(models.Model):
    ''' 学院的学生会 '''
    name = models.CharField(max_length=100)
    introduction = models.TextField()
    chef = models.CharField(max_length=20)
    chef_introduction = models.TextField()

    def __unicode__(self):
        return self.name


class S_news(models.Model):  # 院会的新闻
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='snews')
    video = models.CharField(max_length=200, blank=True)
    exc_editor = models.CharField(max_length=20, default='本新闻执行编辑')
    duty_editor = models.CharField(max_length=20, default='本新闻责任编辑')
    view_num = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=datetime.now())
    school = models.ForeignKey(School)

    def __unicode__(self):
        return self.title


########################################################################
########################################################################


class Information(models.Model):
    datetime = models.DateTimeField(default=datetime.now())
    view_num = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='information', default=None)
    body = models.TextField()
    exc_editor = models.CharField(max_length=20, default='本公告执行编辑')
    duty_editor = models.CharField(max_length=20, default='本公告责任编辑')

    def __unicode__(self):
        return self.title


class Carousel(models.Model):  # Carousel是轮播器的意思
    image = models.ImageField(upload_to='carousel', default=None)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Apply(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    introduction = models.TextField()
    image = models.ImageField(upload_to='apply')
    datetime = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.name


class Safeguard(models.Model):
    name = models.CharField(max_length=20, default='维权者名字')
    title = models.CharField(max_length=200, default='维权主题')
    content = models.TextField()
    datetime = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.title


###################################################################
#               其他一些元素                                        #
###################################################################
# 一些乱起八糟

class SomeElse(models.Model):
    group_frame = models.ImageField()


class Star(models.Model):  # 某月之星
    content = models.CharField(max_length=200)
    image = models.ImageField(upload_to='star', default=None)

    def __unicode__(self):
        return self.content


class WondVideo(models.Model):
    title = models.CharField(max_length=100, default="视频的标题")
    compress_image = models.ImageField(upload_to='wonderful_video', default=None)
    upload_time = models.DateTimeField(default=datetime.now())
    video_url = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class WondPicture(models.Model):
    title = models.CharField(max_length=100, default="图片的标题，不要超过100个字")
    upload_time = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='wonderful_picture')

    def __unicode__(self):
        return self.title


class Academy(models.Model):
    title = models.CharField(max_length=100, default="学术那一栏要填充的字符")
    url = models.CharField(max_length=200, default="这个学术所指向的url")

    def __unicode__(self):
        return self.title


class Rights(models.Model):
    title = models.CharField(max_length=100, default="权益那一栏要填充的字符")
    url = models.CharField(max_length=200, default="这个权益字段所指向的url")

    def __unicode__(self):
        return self.title


class Thoughts(models.Model):
    title = models.CharField(max_length=100, default="思潮那一栏要填充的字符")
    url = models.CharField(max_length=200, default="这个思潮字段所指向的url")

    def __unicode__(self):
        return self.title
