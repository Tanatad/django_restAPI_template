from django.urls import path
from .views import StoreDetailUpdateDelete, StoreList, StoreDeleteAll, ProductDetailUpdateDelete, ProductList, ProductDeleteAll

urlpatterns = [
    # store
    path('stores/', StoreList.as_view(), name='store_list'),
    path('stores/<int:store_id>/',
         StoreDetailUpdateDelete.as_view(), name='store_detail'),
    path('stores/deleteAll/', StoreDeleteAll.as_view(), name='store_delete_all'),
    # product
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:product_id>/',
         ProductDetailUpdateDelete.as_view(), name='product_detail'),
    path('products/deleteAll/',
         ProductDeleteAll.as_view(), name='product_delete_all'),
]
