from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializers


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializers(source='user', read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")
    # email = serializers.EmailField(write_only=True) 'user',
    
    class Meta:
        model= Product
        fields = ['owner', 'title', 'content', 'price', 'salePrice', 'url', 'edit_url', 'public']
    
    # def create(self, validated_data):
    #     # email = validated_data.pop(email)
    #     obj= super().create(validated_data)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop(email)
    #     return super().update(instance, validated_data) 

    def validate_title(self, attrs):
        request = self.context.get('request')
        user = request.user
        qs = Product.objects.filter(title__exact=attrs)
        if qs.exists():
            raise serializers.ValidationError(f"{attrs} name is already taken")
        return (attrs)


    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
