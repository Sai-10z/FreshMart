from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = (
        ('Fruit', 'Fruit'),
        ('Vegetable', 'Vegetable'),
    )

    name = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    # ✅ FIX: allow blank image (prevents crash if not uploaded)
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    # ✅ OPTIONAL (future use - not breaking anything)
    stock = models.IntegerField(
        default=10
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

    # ✅ SAFE IMAGE ACCESS (prevents template crash)
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return '/static/images/default.png'   # fallback image