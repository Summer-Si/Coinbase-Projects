from .models import Product, Historical
from celery import shared_task
import requests
import datetime
from django.utils import timezone

@shared_task
def fetch_data():
    products = Product.objects.all()
    for product in products:
        ticker = product.ticker
        # ?granularity=60: one minute; 300: 5min
        response = requests.get(f'https://api.exchange.coinbase.com/products/{ticker}/candles?granularity=60')
        data = response.json()

        if response.status_code == 200:
            
            for candle in data:
                
                timestamp, low, high, open, close, volume = candle
                timestamp_dt = datetime.datetime.fromtimestamp(timestamp)
                timestamp_aware = timezone.make_aware(timestamp_dt, timezone.get_current_timezone())

                if not Historical.objects.filter(product=product, timestamp=timestamp_aware).exists():
                    # 如果不存在,则创建一个新的Historical记录
                    Historical.objects.create(
                        product=product,
                        timestamp=timestamp_aware,
                        low=low,
                        high=high,
                        open=open,
                        close=close,
                        volume=volume,
                    )