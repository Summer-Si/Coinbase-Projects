from django.urls import path
from . import views
from .views import get_latest_historical_data

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('api/historical-data/<int:pk>/', get_latest_historical_data, name='get_latest_historical_data'),
    path('<int:pk>/update/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
]