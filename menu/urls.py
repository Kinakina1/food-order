from django.urls import path
from menu.views import add_food, food_list

urlpatterns = [
    path('add', add_food, name="add_food"),
    path('list', food_list, name="food_list")
]
