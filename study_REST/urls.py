
from django.contrib import admin
from django.urls import path, include, re_path

from myapp.views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),

    path('api/cats/add/', CategoryAddAPIView.as_view()),
    path('api/cats/show/', CategoryShowAPIView.as_view()),
    path('api/cats/choose/<int:pk>/', CategoryChooseAPIView.as_view()),

    path('api/tasks/add/', TaskAddAPIView.as_view()),
    path('api/tasks/show/', TaskShowAPIView.as_view()),
    path('api/tasks/choose/<int:pk>', TaskChooseAPIView.as_view())

#
]
