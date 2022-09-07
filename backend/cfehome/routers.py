from rest_framework.routers import DefaultRouter
from products.viewset import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
urlpatterns = router.urls
