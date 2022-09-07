from urllib import request
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import Http404


class ProductDetailAPIView(StaffEditorPermissionMixin, UserQuerySetMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'  


class ProductUpdateAPIView(StaffEditorPermissionMixin, UserQuerySetMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  
    

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        # return super().perform_update(serializer)


class ProductDeleteAPIView(StaffEditorPermissionMixin, UserQuerySetMixin ,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class ProductListCreateAPIView(StaffEditorPermissionMixin, UserQuerySetMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        # email = serializer.validated_data.pop('email')
        # print(email)
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user ,content=content, title=title)
        # return super().perform_create(serializer)
    
    # def get_queryset(self):
    #     request = self.request
    #     qs = super().get_queryset()
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     # print(request.user)
    #     return qs.filter(user=request.user)

class ProductMixinView(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  

    def get(self, request, *args, **kwargs):
        print(kwargs, args)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request=request, *args, **kwargs)
    
    def post(self, request, *args, **kwags):
        return self.create(request, *args, **kwags)
    
    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content, title=title)


@api_view(['GET', 'POST'])
def products_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exists():
            #     raise Http404
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data=data)


    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # data = serialize.save()
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content, title=title)
            # print(serializer.data)
            return Response(serializer.data)
        return Response({"detail":"Invalid data"}, status=400)