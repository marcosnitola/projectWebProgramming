from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('maps', views.map, name='map'),
    path('order', views.order, name='order'),
]
