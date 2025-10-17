from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.urls import path, include

def api_welcome(request):
    return JsonResponse({
        "message": "欢迎访问用户管理中心 (SUT)",
        "system": "用户管理系统",
        "version": "1.0.0",
        "endpoints": {
            "admin": "/admin/",
            "api_docs": "/api/",
            "register": "/api/register/",
            "login": "/api/login/",
            "profile": "/api/profile/"
        }
    })

urlpatterns = [
    path('', api_welcome),  # 根路径
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 管理员站点标题
admin.site.site_header = "用户管理中心 (SUT)"
admin.site.site_title = "用户管理中心"
admin.site.index_title = "管理后台"