import datetime
from unittest import TestCase

from advertisement.models import Category, Offer
from advertisement.tests.factories import CategoryFactory, OfferFactory


class CategoryTestCase(TestCase):
    def setUp(self) -> None:
        self.car = CategoryFactory(name="Car", ordering=False)
        self.boat = CategoryFactory(name="Boat", ordering=True)

    def test_category_get(self):
        car = Category.objects.get(name="Car")
        self.assertEqual(car.name, self.car.name)


class OffersTestCase(TestCase):
    def setUp(self) -> None:
        self.offer_1 = OfferFactory(category__name="car", title="BMW", description="M6", price=250000.25,
                                    created_at=datetime.datetime.now())
        self.offer_2 = OfferFactory(category__name="boat", title="Yamaha", description="21FT", price=53799.25,
                                    created_at=datetime.datetime.now())

    def test_offer_get(self):
        offer = Offer.objects.get(title="BMW")
        self.assertEqual(offer.title, self.offer_1.title)
        self.assertEqual(offer.category.name, "car")
