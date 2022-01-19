from http.client import HTTPResponse
from django.shortcuts import render
from pytz import timezone
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from django.http  import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone

# Create your views here.

def order_list(request, shop):
    if request.method == 'GET':
        order_list = Order.objects.filter(shop=shop)
        return render(request, 'boss/order_list.html', {'order_list': order_list})

@csrf_exempt
def time_input(request):
    if request.method == 'POST':
        estimated_time = request.POST['estimated_time']
        order_id = request.POST['order_id']
        order_item = Order.objects.get(pk=order_id)
        shop = order_item.shop.id
        order_item.estimated_time = int(estimated_time)
        order_item.save()
        return render(request, 'boss/success.html', {'shop': shop})
    else:
        return HttpResponse(status=404)