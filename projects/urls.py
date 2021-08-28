from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('1/', views.show),
    # path('/<int:id>/', views.ProjectView.as_view()),  # 语法错误，前面多了一个 '/' 号

    # path('<int:id>/', views.ProjectView.as_view()),     # 类视图
    # 这个类视图不能path('<int:pk>/', views.ProjectDetailView.as_view()), 同时存在

    path('', views.ProjectViewNP.as_view()),     # 类视图
    path('<int:pk>/', views.ProjectDetailView.as_view()),     # 类视图

    # re_path(r'^(?P<username>\w{6,12})/$', views.get_users),  # 最后一个'/'不要忘了
]
