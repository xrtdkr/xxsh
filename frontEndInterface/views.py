# coding=utf-8

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from frontEndInterface.models import *
from django.utils import timezone


# Create your views here.

def index(request):
    if request.method == 'GET':
        ret_dict = {}

        # 轮播图模块
        ret_carousel_list = []
        for carousel in Carousel.objects.all():
            ele_dict = {}

            ele_dict['url'] = None
            ele_dict['image'] = carousel.image.url
            ret_carousel_list.append(ele_dict)
        ret_dict['carousel'] = ret_carousel_list

        # 校会新闻
        ret_xnews_list = []
        for xnew in X_news.objects.all().order_by('datetime')[0:8]:
            ele_dict = {}

            # 决定是不是有new这个小标签
            deltatime = datetime.now() - xnew.datetime.replace(tzinfo=None)
            if deltatime.days >= 7:
                new_flag = False
            else:
                new_flag = True
            ele_dict['newFlag'] = new_flag

            # 决定校会新闻的标题
            title = xnew.title
            ele_dict['title'] = title

            # 把东西放到list里面去
            ret_xnews_list.append(ele_dict)
        # 把list放到返回的大字典里面去
        ret_dict['xNews'] = ret_xnews_list

        # 院会新闻
        ret_snews_list = []
        for snew in S_news.objects.all().order_by('datetime')[0:8]:
            ele_dict = {}

            # 决定是不是有new这个小标签
            deltatime = datetime.now() - snew.datetime.replace(tzinfo=None)
            if deltatime.days >= 7:
                new_flag = False
            else:
                new_flag = True
            ele_dict['newFlag'] = new_flag

            title = snew.title
            ele_dict['title'] = title

            ret_xnews_list.append(ele_dict)
        ret_dict['sNews'] = ret_snews_list

        # 信息公告
        ret_info_list = []
        for info in Information.objects.all().order_by('datetime')[0:6]:
            ele_dict = {}
            deltatime = datetime.now() - info.datetime.replace(tzinfo=None)
            if deltatime.days >= 7:
                new_flag = False
            else:
                new_flag = True
            ele_dict['newFlag'] = new_flag

            title = info.title
            ele_dict['title'] = title

            ret_info_list.append(ele_dict)
        ret_dict['information'] = ret_info_list

        # 学联活动推荐
        ret_xact_list = []
        for xact in X_activity.objects.all().order_by('datetime')[0:4]:
            ele_dict = {}
            ele_dict['title'] = xact.name

            ret_xact_list.append(ele_dict)
        ret_dict['xActivity'] = ret_xact_list

        # 学术
        ret_academy_list = []
        for aca in Academy.objects.all():
            ele_dict = {}
            ele_dict['title'] = aca.title
            ele_dict['url'] = aca.url

            ret_academy_list.append(ele_dict)
        ret_dict['academy'] = ret_academy_list

        # 权益
        ret_rights_list = []
        for right in Rights.objects.all():
            ele_dict = {}
            ele_dict['title'] = right.title
            ele_dict['url'] = right.url

            ret_rights_list.append(ele_dict)

        ret_dict['rights'] = ret_rights_list

        # 思潮
        ret_thou_list = []
        for thou in Thoughts.objects.all():
            ele_dict = {}
            ele_dict['title'] = thou.title
            ele_dict['url'] = thou.url

            ret_thou_list.append(ele_dict)

        ret_dict['thoughts'] = ret_thou_list

        # xx月之星
        ret_star_list = []
        for star in Star.objects.all():
            ele_dict = {}
            ele_dict['title'] = star.content
            ele_dict['imageUrl'] = star.image.url

            ret_star_list.append(ele_dict)

        ret_dict['star'] = ret_star_list

        # 精彩视频
        ret_video_list = []
        ele_dict = {}
        ele_dict['imageUrl'] = WondVideo.objects.all()[0].compress_image.url
        ret_video_list.append(ele_dict)
        ret_dict['wonderfulVideo'] = ret_video_list

        # 精彩图片
        ret_image_list = []
        ele_dict = {}
        ele_dict['imageUrl'] = WondPicture.objects.all()[0].image.url
        ret_image_list.append(ele_dict)
        ret_dict['wonderfulImage'] = ret_image_list

        return JsonResponse(ret_dict)

    else:
        return HttpResponse('fail')

def
