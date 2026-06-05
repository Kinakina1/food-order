from django.urls import path
from orders.views import add_to_cart, cart, decrease_item, increase_item, checkout

urlpatterns = [
    path('', cart, name="cart"),
    path("add/<int:food_id>", add_to_cart, name="add_to_cart"),
    path('increase_item/<int:food_id>', increase_item, name="increase_item"),
    path('decrease_item/<int:food_id>', decrease_item, name="decrease_item"),
    path('checkout/', checkout, name="checkout"),
]
