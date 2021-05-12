from django_filters import rest_framework as filters

from advertisement.models import Offer


class OfferFilter(filters.FilterSet):
    """
    Filtering the list of offers by category ID.
    """
    category = filters.BaseInFilter()

    class Meta:
        model = Offer

        fields = ('category',)
