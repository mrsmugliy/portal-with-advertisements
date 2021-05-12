from django_filters import rest_framework
from rest_framework import viewsets

from advertisement.models import Offer, Category
from advertisement.serializers import CategorySerializer
from advertisement.filters import OfferFilter

from advertisement.service import OfferMixin


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet to enumerate a category, get one category, create a new category, update a category, and delete.
    """
    queryset = Category.objects.all().order_by('-ordering')
    serializer_class = CategorySerializer


class OfferViewSet(OfferMixin, viewsets.ModelViewSet):
    """
    A ViewSet to enumerate a, get one offer, create a new offer, update a offer, and delete.
    """
    queryset = Offer.objects.all()
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = OfferFilter
