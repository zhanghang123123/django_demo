from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def show(request):
    return HttpResponse(" nihao a ")


def get_project(request):
    return HttpResponse("<h1>这个一个项目</h1>")


def get_project_by_id(request, id):
    if isinstance(id, int) and id < 100:
        return HttpResponse(f"这个一个id为 {id} 的项目")
    else:
        return HttpResponse(f"这个id为 {id} 的项目不存在！")


def get_users(request, username):
    return HttpResponse(f"这个一个用户为 {username} 的项目")