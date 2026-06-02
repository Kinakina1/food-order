from django.urls import path
from menu.views import add_food

urlpatterns = [
    path('add', add_food, name="add_food")
]
