from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from projects.models import Projects
from interfaces.models import Interfaces
import json


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
        # 添加数据方法一
        # onemethod_object = Projects(name='在线商城2', leader='mrf2')
        # onemethod_object.save()
        # 添加数据方法二（推荐，不用save）
        twomethod_object = Projects.objects.create(name='在线商城4', leader='mrf4', is_execute=False, description='好项目')

        # 创建从表数据
        # 关联父表
        #   > 先获取到父表模型对象
        project_1 = Projects.objects.get(id=1)
        twomethod_object = Interfaces.objects.create(name='登陆接口',
                                                     tester='mrf3',
                                                     projects=project_1)  # 必须填，要关联父表 或projects_id=project_1.id

        #####
        # a. 从数据库中读取数据项目
        # b. 数据自动填充到html 模板中
        datas = [
            {
                "project_name": "前程贷项目1",
                "leader": "kk",
                "app_name": "p2p平台应用1",
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
        ret = JsonResponse(datas, safe=False, status=200, json_dumps_params={'ensure_ascii': False})
        return ret

    def post(self, request, *args, **kwargs):
        # post 的一些列操作
        one_object = Projects(name='在线商城', leader='mrf')
        one_object.save()
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


class ProjectViewNP(View):
    def get(self, request):
        """
        GET /projects/ 获取所有的项目数据（将说有的数据已json数组的形式返回）
        :param request:
        :return:
        """
        # 1. 从数据库中读取所有的数据
        obj = Projects.objects.all()  # queryset类型数据
        # 2. 将项目QuerySet对象转化为嵌套字典的列表数据
        projects_list = []
        for obji in obj:
            obji: Projects
            projects_list.append({
                "id": obji.id,
                "name": obji.name,
                "is_exicute": obji.is_execute,
            })
        # 3. 嵌套字典的列表数据转化为json数据返回值前端
        return JsonResponse(projects_list, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        """
        POST /projects/     创建一条项目数据（前端以json形式传递项目参数，创建成功后将项目数据以json对象形式返回）
        :param request:
        :return:
        """
        # 1. 从前端获取项目数据
        #       需要对前端传递的数据进行判断
        #       传递数据校验（要存入数据库中的数据需要校验是否符合格式）
        try:
            python_dict = json.loads(request.body, encodings='utf-8')
        except Exception as e:
            return JsonResponse({
                'msg': '参数有误',
                'status': 1,
            }, status=400)
        # 2. 前端请求参数数据校验
        name = python_dict.get('name')  # 这种方式取值 更好，python_dict['name'] 取值有时候会有空值就会报错
        if name is None:
            return JsonResponse({
                'msg': '未传递项目名称',
                'status': 1,
            }, status=400)
        elif not isinstance(name, str):  # 判断数据类型
            return JsonResponse({
                'msg': '项目名称必须为字符串类型',
                'status': 1,
            }, status=400)
        elif Projects.objects.filter(name=name).exists():
            return JsonResponse({
                'msg': '项目名称已经存在',
                'status': 1,
            }, status=400)
        elif len(name) > 50:
            return JsonResponse({
                'msg': '项目名称长度不能超过50个字节',
                'status': 1,
            }, status=400)

        leader = python_dict.get('leader')
        is_excute = python_dict.get('is_excute')
        # 3. 创建项目数据
        Projects.objects.create(name=python_dict.get("name"),
                                leader=python_dict.get("leader"),
                                is_excute=python_dict.get("is_excute"), )
        # 这里的写法很鸡肋，如果有200个对象呢？#
        try:
            Projects.objects.create(**python_dict)  # 默认上述校验完成后，数据字段完整，拆包就没问题了，为了严谨 用try
        except Exception as e:
            return JsonResponse({
                'msg': '参数有误',
                'status': 1,
            }, status=400)

        # 4. 将模型对象转化为字典
        return_dict = {
            "id": obji.id,
            "name": obji.name,
            "is_exicute": obji.is_execute,
        }
        # 5. 将字典返回至前端
        return JsonResponse(return_dict, safe=False, json_dumps_params={'ensure_ascii': False})


class ProjectDetailView(View):
    def get(self, request, pk):
        """
        GET /projects/pk/  获取某一条项目数据(将这一条项目数据以json对象返回)
        :param request:
        :param pk:
        :return:
        """
        # 1. 从数据库中获取项目的模型对象
        #   pk一定是int类型，因为url已经匹配成功了
        try:
            obji = Projects.objects.get(id=pk)  # 获取数据都要考虑失败的情况
        except Exception:
            return JsonResponse({
                'msg': '参数有误',
                'status': 1,
            }, status=400)

        # 2. 将模型对象转化为字典
        return_dict = {
            "id": obji.id,
            "name": obji.name,
            "is_exicute": obji.is_execute,
            "leader": obji.leader,
        }
        # 3. 将项目的字典数据返回值前端
        return JsonResponse(return_dict, safe=False, json_dumps_params={'ensure_ascii': False})

    def put(self, request, pk):
        # 1. 从前端获取项目数据
        #       需要对前端传递的数据进行判断
        #       传递数据校验（要存入数据库中的数据需要校验是否符合格式）
        try:
            python_dict = json.loads(request.body, encodings='utf-8')
        except Exception as e:
            return JsonResponse({
                'msg': '参数有误',
                'status': 1,
            }, status=400)
        # 2. 前端请求参数数据校验
        name = python_dict.get('name')  # 这种方式取值 更好，python_dict['name'] 取值有时候会有空值就会报错
        if name is None:
            return JsonResponse({
                'msg': '未传递项目名称',
                'status': 1,
            }, status=400)
        elif not isinstance(name, str):  # 判断数据类型
            return JsonResponse({
                'msg': '项目名称必须为字符串类型',
                'status': 1,
            }, status=400)
        elif Projects.objects.filter(name=name).exists():
            return JsonResponse({
                'msg': '项目名称已经存在',
                'status': 1,
            }, status=400)
        elif len(name) > 50:
            return JsonResponse({
                'msg': '项目名称长度不能超过50个字节',
                'status': 1,
            }, status=400)

        # 3. 从数据库中读取id 为pk的项目模型对象
        try:
            obji = Projects.objects.get(id=pk)  # 获取数据都要考虑失败的情况
        except Exception:
            return JsonResponse({
                'msg': '参数有误',
                'status': 1,
            }, status=400)
        # 4. 更新项目
        obji.name = python_dict.get("name") or obji.name  # 如果前端没传 就更新原来的值（当然如果前面没做校验）
        obji.leader = python_dict.get("leader") or obji.leader
        obji.is_execute = python_dict.get("is_execute") or obji.is_execute
        obji.description = python_dict.get("description") or obji.description
        obji.save()

        # 3~4步骤可以写为：
        # Projects.objects.filter(id=pk).update(**python_dict)
        # 5. 更新后的模型对象，转化为字典
        return_dict = {
            "id": obji.id,
            "name": obji.name,
            "is_exicute": obji.is_execute,
            "leader": obji.leader,
        }
        # 6. 将字典数据返回至前端
        return JsonResponse(return_dict, safe=False, json_dumps_params={'ensure_ascii': False})
        pass

    def delete(self, request, pk):
        # 1. 从数据库中读取id 为pk的项目模型对象
        try:
            obji = Projects.objects.get(id=pk)  # 获取数据都要考虑失败的情况
        except Exception:
            return JsonResponse({
                'msg': '参数有误',
                'status': 1,
            }, status=400)
        # 2. 删除模型对象
        obji.delete()
        # 3. 返回空至前端
        # return JsonResponse(None, status=204) #会报500的错误，None参数不能转换为Json数据
        return HttpResponse(None, status=204)