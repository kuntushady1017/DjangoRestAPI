from rest_framework import serializers


class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)

class UserPublicSerializers(serializers.Serializer):
    username =serializers.CharField(read_only=True)
    id =serializers.IntegerField(read_only=True)    
    # other_products = serializers.SerializerMethodField(read_only=True)


    # def get_other_products(self, obj):
    #     request =self.context.get('request')
    #     user_product = obj.product_set.all()[:5]
    #     return UserProductInlineSerializer(user_product, many=True, context=self.context).data