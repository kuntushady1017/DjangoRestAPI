from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.
# @api_view(['GET'])
@api_view(['POST'])
def apiHome(request, *args, **kwargs):
    """ DRF API View """
    instance = Product.objects.all().order_by("?").first()
    # data = {}
    serialize = ProductSerializer(data=request.data)
    if serialize.is_valid(raise_exception=True):
        # data = serialize.save()
        print(serialize.data)
    # if instance:
    #     # data = model_to_dict(modelData, fields=['id','title', 'content', 'price', 'salePrice'])
    #     data = ProductSerializer(instance=instance).data
        return Response(serialize.data)
    return Response({"detail":"Invalid data"}, status=400)
