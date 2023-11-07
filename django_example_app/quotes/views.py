from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Product, Section

# Create your views here.
def main(request):
    return render(request, 'quotes/main.html')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SectionViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Section.objects.all()
    serializer_class = SectionSerializer