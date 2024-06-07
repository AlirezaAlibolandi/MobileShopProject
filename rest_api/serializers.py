from rest_framework import serializers
from shop_module.models import Product ,Category,Company,Images
from blog_module.models import Article

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','title','slug','price','stock','short_description','description','weight','size']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
