from rest_framework import serializers

from advertisement.models import Offer, Category


class CategorySerializer(serializers.ModelSerializer):
    """
    List of category.
    """

    class Meta:
        model = Category
        fields = '__all__'


class OffersListSerializer(serializers.ModelSerializer):
    """
    List of offers.
    """

    class Meta:
        model = Offer
        exclude = ('description', 'created_at')


class OfferDetailSerializer(serializers.ModelSerializer):
    """
    Detail offer with all category fields.
    """
    category = CategorySerializer()

    class Meta:
        model = Offer
        fields = ('id', 'title', 'description', 'price', 'created_at', 'category')


class OfferCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Create and update offer.
    """

    class Meta:
        model = Offer
        fields = '__all__'
