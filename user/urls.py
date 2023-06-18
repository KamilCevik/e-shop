from . import views
from django.urls import path

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('update', views.user_update, name='user_update'),
    path('password', views.change_password, name='change_password'),
    path('orders', views.user_orders, name='user_orders'),
    path('orderdetail/<int:id>', views.orderdetail, name='orderdetail'),
    path('comments', views.comments, name='comments'),
    path('deletecomment/<int:id>',
         views.deletecomment, name='deletecomment'),
]
