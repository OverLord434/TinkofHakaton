import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', lambda request: redirect('users:home', permanent=True)),
    path('users/', include('users.urls', namespace='users')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('main/', include('main.urls', namespace='main'))
]
