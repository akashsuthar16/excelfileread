from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.home,name="index"),
    # path('reg/',views.reg_user,name="reg"),
    # path('regis/',views.register,name="regis"),
    # path('update/<int:pk>',views.user_upd,name="update"),
    # path('update-user/<int:pk>',views.upd,name="updateuser"),
    # path('delete/<int:pk>',views.dels,name="delete"),
    # file 
    path('',views.fileindex,name="file-index"),
    path('filepage/',views.filepage,name="filepage"),
    path('file-=-upd',views.file_upd,name="file=upd"),
    path('qwe/<int:pk>/',views.abc,name="qwe"),
    path('exce_file/<int:pk>',views.exce_file,name="excefile")
]