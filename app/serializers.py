from rest_framework import serializers
from .models import Store, Product, Sale

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'store_location']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_timestamp']

class SaleSerializer(serializers.ModelSerializer):
    class CustomProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ['product_id', 'product_name']
    store = StoreSerializer()
    product = CustomProductSerializer()
    class Meta:
        model = Sale
        fields = ['transaction_id', 'transaction_date', 'transaction_time', 'transaction_qty', 'unit_price', 'product_category', 'product_detail', 'store', 'product']

    
