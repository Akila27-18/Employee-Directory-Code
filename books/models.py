from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # ✅ Add this
    category = models.ManyToManyField('Category')  # See Issue 2 for fixing this reference

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
