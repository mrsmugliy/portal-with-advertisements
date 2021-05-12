from advertisement.serializers import OffersListSerializer, OfferDetailSerializer, OfferCreateUpdateSerializer


class OfferMixin:
    def get_serializer_class(self):
        """
        Return serializer class based on request.
        """
        if self.action == 'list':
            return OffersListSerializer
        elif self.action == 'retrieve':
            return OfferDetailSerializer
        elif self.action == 'create':
            return OfferCreateUpdateSerializer
        elif self.action == 'update':
            return OfferCreateUpdateSerializer
        return OffersListSerializer
