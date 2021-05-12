from django.contrib import admin

# Register your models here.
from advertisement.models import Category, Offer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass