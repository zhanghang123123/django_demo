from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def show(request):
    return HttpResponse(" nihao a ")


def get_project_by_id(request, id):
    if isinstance(id, int) and id < 100:
        return HttpResponse(f"这个一个id为 {id} 的项目")
    else:
        return HttpResponse(f"这个id为 {id} 的项目不存在！")


def get_users(request, username):
    return HttpResponse(f"这个一个用户为 {username} 的项目")


class ProjectView(View):
    def get(self, request, *args, **kwargs):
        # get 的详细操作
        # return HttpResponse(f"<h1>获取这个{kwargs.get(id)}项目</h1>") # 语法错误，get方法中是 ""
        return HttpResponse(f"<h1>获取这个{kwargs.get('id')}项目</h1>")

    def post(self, request, *args, **kwargs):
        # post 的一些列操作
        return HttpResponse("<h1>修改这个项目</h1>")

    def put(self, request, *args, **kwargs):
        return HttpResponse("<h1>提交一个项目</h1>")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("<h1>删除这个项目</h1>")


"""函数视图（下）被 类视图（上）替代了"""
# def get_project(request):
#     print(type(request))
#     print(request)
#     print(request.method)
#     if request.method == 'GET':
#         # get 的详细操作
#         return HttpResponse("<h2>获取这个项目</h2>")
#     elif request.method == 'POST':
#         # post 的一些列操作
#         return HttpResponse("<h1>修改这个项目</h1>")
#     elif request.method == 'PUT':
#         return HttpResponse("<h1>提交一个项目</h1>")
#     elif request.method == 'DELETE':
#         return HttpResponse("<h1>删除这个项目</h1>")
#     else:
#         return HttpResponse("<h1>这是一个有其他请求方式的项目</h1>")
