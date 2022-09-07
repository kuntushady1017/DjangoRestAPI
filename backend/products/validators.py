from .models import Product
from rest_framework import serializers

def validate_title(attrs):
        qs = Product.objects.filter(title__exact=attrs)
        if qs.exists():
            raise serializers.ValidationError(f"{attrs} name is already taken")
        return (attrs)