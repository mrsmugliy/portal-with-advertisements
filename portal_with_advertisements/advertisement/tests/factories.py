import datetime

import factory

from advertisement.models import Category, Offer


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'Car'
    ordering = False


class OfferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Offer

    category = factory.SubFactory(CategoryFactory)
    title = "BMW"
    description = "M6"
    price = 250000.00
    created_at = datetime.datetime.now()
