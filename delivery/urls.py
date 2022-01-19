
from django.contrib import admin
from django.urls import path, include
from delivery import views

urlpatterns = [
    path('orders/', views.order_list, name="order_list")
    # path('shops/', views.shop, name="shop"),
    # path('menus/<int:shop>', views.menu, name='menu'),
    # path('order/', views.order, name='order')
    # path('snippets/<int:pk>/', views.snippet_detail),
]
