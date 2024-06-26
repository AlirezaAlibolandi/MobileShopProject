"""
URL configuration for MobileShopProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_module.urls')),
    path('account/', include('account_module.urls')),
    path('blog/', include('blog_module.urls')),
    path('shop/', include('shop_module.urls')),
    path('order/', include('order_module.urls')),
    path('api/', include('rest_api.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'ادمین موبایل شاپ'
admin.site.site_title = 'ادمین موبایل شاپ'
admin.site.index_title = 'به پنل ادمین موبایل شاپ خوش آمدید'