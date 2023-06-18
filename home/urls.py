from . import views
from django.urls import include, path


urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('references', views.references, name='references'),
    path('contact', views.contact, name='contact'),
    path('category/<int:id>/<slug:slug>',
         views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>',
         views.product_detail, name='product_detail'),
    path('search/', views.product_search, name='product_search'),
    path('search_auto/', views.get_products, name='get_products'),



]
