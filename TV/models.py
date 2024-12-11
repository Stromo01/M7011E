from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class TV(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    brand = models.CharField(max_length=20, help_text='Brand name')
    model = models.CharField(max_length=20, help_text='Model name')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Price of TV')
    resolution = models.CharField(max_length=20, help_text='Resolution of TV')
    tv_id = models.AutoField(help_text='TV ID',primary_key=True)
    stock = models.IntegerField(help_text='Stock of TV')
    screen_size = models.DecimalField(max_digits=10, decimal_places=2, help_text='Screen size of TV')

    # …

    # Metadata
    class Meta:
        ordering = ['-brand']
        db_table = 'TV'

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('tv-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.brand
    

class Cart(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    user = models.ForeignKey(User, help_text='User ID', on_delete=models.CASCADE)
    cart_id = models.AutoField(help_text='Cart ID', primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    # …

    # Metadata
    class Meta:
        db_table = 'Cart'

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('cart-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f"Cart {self.cart_id} for user {self.user.username}"  # Ensure this returns a string
    
class Cart_Items(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    cart_item_id = models.AutoField(help_text='Cart Item ID',primary_key=True)
    cart = models.ForeignKey(help_text='Cart ID',on_delete=models.CASCADE, to='Cart')
    tv = models.ForeignKey(help_text='TV ID',on_delete=models.CASCADE, to='TV')
    quantity = models.IntegerField(help_text='Quantity of TV in cart')
    # …

    # Metadata
    class Meta:
        db_table = 'Cart_Items'
        unique_together = ('cart', 'tv_id')

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('cart_items-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f"Cart {self.cart.cart_id} has {self.quantity} {self.tv.brand} {self.tv.model}"
    
class Review(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    review_id = models.AutoField(help_text='Review ID',primary_key=True)
    tv = models.ForeignKey(help_text='TV ID',on_delete=models.CASCADE, to='TV')
    user = models.ForeignKey(help_text='User ID',on_delete=models.CASCADE, to='auth.User')
    rating = models.IntegerField(help_text='Rating of TV')
    review_text = models.TextField(help_text='Review of TV')
    # …

    # Metadata
    class Meta:
        db_table = 'Review'
        unique_together = ('tv', 'user')

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('review-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f"Review of {self.tv.brand} {self.tv.model} by {self.user.username}"