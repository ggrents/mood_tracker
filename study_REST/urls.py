
from django.contrib import admin
from django.urls import path, include, re_path

from myapp.views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .yasg import urlpatterns as urls_doc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),

    path('api/cats/add/', CategoryAddAPIView.as_view(), name='category-create'),
    path('api/cats/show/', CategoryShowAPIView.as_view(), name='category-list'),
    path('api/cats/<int:pk>/', CategoryChooseAPIView.as_view(), name='category-detail'),

    path('api/tasks/add/', TaskAddAPIView.as_view(), name='task-create'),
    path('api/tasks/show/', TaskShowAPIView.as_view(), name='task-list'),
    path('api/tasks/<int:pk>', TaskChooseAPIView.as_view(), name = 'task-detail')

]

urlpatterns+=urls_doc