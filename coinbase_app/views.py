from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Historical
from django.http import JsonResponse
import requests
import datetime
from django.utils import timezone

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        name = request.POST['name']
        product = Product(ticker=ticker, name=name)
        product.save()
        return redirect('product_list')
    return render(request, 'product_create.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    historical_data = Historical.objects.filter(product=product).order_by('-timestamp')
    # call fetch_data
    # fetch_data.delay()
    return render(request, 'product_detail.html', {'product': product, 'historical_data': historical_data})

def get_latest_historical_data(request, pk):
    product = get_object_or_404(Product, pk=pk)
    latest_data = Historical.objects.filter(product=product).order_by('-timestamp')
    data = []
    for item in latest_data:
        timestamp_str = item.timestamp.strftime("%b %d, %Y, %I:%M %p").replace('AM', 'a.m.').replace('PM', 'p.m.')
        timestamp_str = timestamp_str[0].upper() + timestamp_str[1:]
        data.append({
            'timestamp': timestamp_str,
            'open': item.open,
            'high': item.high,
            'low': item.low,
            'close': item.close,
            'volume': "{:.2f}".format(item.volume),
        })
    return JsonResponse(data, safe=False)

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.ticker = request.POST['ticker']
        product.name = request.POST['name']
        product.save()
        return redirect('product_detail', pk=product.pk)
    return render(request, 'product_update.html', {'product': product})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})
