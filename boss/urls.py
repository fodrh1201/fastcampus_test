
from django.contrib import admin
from django.urls import path, include
from boss import views

urlpatterns = [
    path('orders/<int:shop>', views.order_list, name="order_list"),
    path('timeinput/', views.time_input, name="timeinput")
    # path('menus/<int:shop>', views.menu, name='menu'),
    # path('order/', views.order, name='order')
    # path('snippets/<int:pk>/', views.snippet_detail),
]
