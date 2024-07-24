from rest_framework import serializers
from .models import MenuItem,Category
from decimal import Decimal




class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class MenuItemSerializer(serializers.ModelSerializer):
    item_description = serializers.CharField(source='description')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','item_description', 'price_after_tax','category','category_id']
    def calculate_tax(self, product:MenuItem):
        return round(product.price * Decimal(1.1),2)

'''
class MenuItemSerialzer(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = ['id' , 'title' , 'price' , 'description', 'category']
        extra_kwargs = {'price':{'min_value':2},
                        }

'''