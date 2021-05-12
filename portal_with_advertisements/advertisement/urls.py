from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from advertisement.views import OfferViewSet, CategoryViewSet

urlpatterns = format_suffix_patterns([
    path('category/', CategoryViewSet.as_view({'get': 'list', })),
    path('category/<int:pk>',
         CategoryViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'post': 'create'})),
    path('offers/', OfferViewSet.as_view({'get': 'list'})),
    path('offers/<int:pk>',
         OfferViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'post': 'create'})),
])
