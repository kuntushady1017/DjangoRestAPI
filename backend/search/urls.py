from django.urls import path
from .views import SearchListAPIView, SearchIndexListAPIView

urlpatterns = [
    # path('', SearchListAPIView.as_view(), name='search'),
    path('', SearchIndexListAPIView.as_view(), name="search"),
]