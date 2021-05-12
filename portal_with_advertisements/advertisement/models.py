from django.db import models


class Category(models.Model):
    """
    Category for portal with advertisements.
    """
    name = models.CharField(max_length=50, verbose_name="Name of category")
    ordering = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Offer(models.Model):
    """
    Offer for category.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Offer category")
    title = models.CharField(max_length=50, verbose_name="Title of offer")
    description = models.CharField(max_length=250, verbose_name="Description of offer")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price of offer")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date and time of creation of the offer")

    def __str__(self):
        return f'{self.category}, {self.title}'
