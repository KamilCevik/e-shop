"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from order.views import shopcart

from user.views import loginUser,logoutUser,register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('user/', include('user.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # The CKEditor path
    path('shopcart/', shopcart, name='shopcart'),

    path('login/', loginUser, name='loginUser'),
    path('logout/', logoutUser, name='logoutUser'),
    path('register/', register, name='register'),

]
# + static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
