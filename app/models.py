from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


# Product Model
class Product (models.Model):
    # Choices for suitable sex for the product
    class Sexes (models.TextChoices):
        MALE = 'Men', _('Men')
        FEMALE = 'Women', _('Women')

    # Choices for size of the product
    class Sizes (models.TextChoices):
        SMALL = 'S', _('Small')
        MEDIUM = 'M', _('Medium')
        LARGE = 'L', _('Large')
        XTRALARGE = 'XL', _('ExtraLarge')
        XXTRALARGE = 'XXL', _('XXtraLarge')

    # Title or name of the product
    title = models.CharField(max_length=100)

    # Size of the product
    size = models.CharField(
        max_length = 3,
        choices = Sizes.choices,
        default = Sizes.SMALL
    )

    # Undiscounted Price
    orignal_price = models.PositiveSmallIntegerField ()

    # Discounted Price
    current_price = models.PositiveSmallIntegerField()

    # Color of the product
    color = models.CharField(max_length=50)

    # Avaibility of the product
    available = models.BooleanField(default=True)

    # Category foreign key!
    # category = models.FIGUREOUT

    # Sex for product
    sex = models.CharField(
        max_length = 5,
        choices = Sexes.choices
    )

    # Product Descriptions
    description = models.TextField()

    # Fitting details
    fitting = models.TextField(default="Comfort Fit")

    # Product Image 1
    img1 = models.ImageField(upload_to='media/products')

    # Product Image 2
    img2 = models.ImageField(upload_to='media/products')


# Category model
class Category (models.Model):
    # Choices for suitable sex for the category
    class Sexes (models.TextChoices):
        MALE = 'Men', _('Men')
        FEMALE = 'Women', _('Women')

    # Title of the Category
    title = models.CharField(max_length=200)

    # Type of category i.e., is it suitable for Man or women
    type = models.CharField(
        max_length = 5,
        choices = Sexes.choices
    )
