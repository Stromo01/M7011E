from django.contrib import admin

# Register your models here.
from .models import TV,Cart,Cart_Items,Review

@admin.register(TV)
class TVAdmin(admin.ModelAdmin):
    list_display = ('tv_id' ,'brand', 'model', 'price', 'resolution', 'stock', 'screen_size')
    fields = ['brand', 'model', 'price', 'resolution', 'stock', 'screen_size']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user' ,'cart_id', 'created_at')
    fields = []

@admin.register(Cart_Items)
class Cart_ItemsAdmin(admin.ModelAdmin):
    list_display = ('cart_item_id','quantity','tv_id','cart')
    fields = ['quantity','tv','cart']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id','tv_id','user','rating','review_text')
    fields = ['rating','review_text','tv','user']

