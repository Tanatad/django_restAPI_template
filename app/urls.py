from django.urls import path
from .views import StoreDetailUpdateDelete, StoreList
from .views import ProductList, ProductDetailUpdateDelete
from .views import SaleList, SaleDetailUpdateDelete

urlpatterns = [
    path('stores/', StoreList.as_view(), name='store_list'),
    path('stores/<int:store_id>/',
         StoreDetailUpdateDelete.as_view(), name='store_detail'),

    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:store_id>/',
         ProductDetailUpdateDelete.as_view(), name='product_detail'),

    path('sales/', SaleList.as_view(), name='sale_list'),
    path('sales/<int:store_id>/',
         SaleDetailUpdateDelete.as_view(), name='sale_detail'),          
]
