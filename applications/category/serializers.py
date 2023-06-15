from rest_framework import serializers
from .models import Category

class CategorySerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'title']
        read_only_fields = ['slug']
        