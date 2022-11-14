from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop,Menu,Order,Orderfood
from order.serlizers import ShopSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def shop(request):
    if request.method == 'GET':
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop, many=True) # serializer--> jso형태로 바꿔준다
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# Create your views here.
