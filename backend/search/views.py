from rest_framework import generics
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from . import client

class SearchListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        result = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            result = qs.search(q, user=user)
        return result


class SearchIndexListAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        query =  request.GET.get('q')
        tag = request.GET.get('tag') or None
        public = str(request.GET.get('public')) != "0"
        if not query:
            Response("", status=404)
        result = client.perform_search(query, tags=tag, user=user, public=public) 
        return Response(result)