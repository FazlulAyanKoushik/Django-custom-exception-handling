from django.core.management.base import BaseCommand
from product.models import Product


class Command(BaseCommand):
    help = "Create a product"

    def handle(self, *args, **kwargs):
        """Creating 10 products"""
        for i in range(10):
            Product.objects.create(
                name=f"Product {i}",
                price=10.00,
                category="Category",
                sub_category="Sub Category",
                brand="Brand",
                description="Description",
            )
        self.stdout.write(self.style.SUCCESS("Products created successfully"))
