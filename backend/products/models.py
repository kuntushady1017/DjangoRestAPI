import random
from django.db import models
from django.db.models import Q
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


TAGS_MODEL_VALUES = ['clothes', 'shoes', 'cars', 'movies', 'camera', 'boats', 'electronics']


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup_field = Q(title__icontains=query) | Q(content__icontains=query) 
        qs = self.is_public().filter(lookup_field)
        if user is not None:
            qsUser = self.filter(user=user).filter(lookup_field)
            qs = (qs | qsUser).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    def search(self, query, user=None):
        return self.get_queryset().search(query=query, user=user)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]

    def is_public(self) -> bool:
        return self.public

    def __str__(self) -> str:
        return self.title
    
    @property
    def salePrice(self):
        return "%.2f" %(float(self.price) * 0.18)
    
    @property
    def body(self):
        return self.content
    
    def get_discount(self):
        return(float(self.price) * 0.5)