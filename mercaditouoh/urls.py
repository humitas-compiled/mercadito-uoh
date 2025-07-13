"""
URL configuration for mercaditouoh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
"""from login import views as login_views #importa tu vista login_view
from compras import views as compras_views
from vender import views """

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('compras/', include('compras.urls')),
    path('vender/', include('vender.urls')),
    path('chats/', include('chat.urls')),
    path('perfil/', include('perfil_user.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
