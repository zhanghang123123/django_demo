from django.http import HttpResponse, JsonResponse
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
        # return HttpResponse(f"<h1>获取这个{kwargs.get('id')}项目</h1>")

        #####
        # a. 从数据库中读取数据项目
        # b. 数据自动填充到html 模板中
        datas = [
            {
                "project_name" : "前程贷项目1",
                "leader" : "kk",
                "app_name" : "p2p平台应用1",
            },
            {
                "project_name": "前程贷项目2",
                "leader": "hang",
                "app_name": "p2p平台应用2",
            },
            {
                "project_name": "前程贷项目3",
                "leader": "zhang",
                "app_name": "p2p平台应用3",
            },
        ]
        # return render(request, 'index.html', locals())  # render 渲染html
        # 上面直接返回（render）的是一个html模板，是前后端不分离的模式
        # 下面返回的是数据，将前端和后段分离开来，返回的是数据, 这样不仅可以给html用，还可以给手机
        # （不管是安卓还是IOS）APP，小程序等用
        return JsonResponse(datas, safe=False, status=200, json_dumps_params={'ensure_ascii': False})

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
