from django.urls import path
from menu.views import add_food, food_list, category_detail ,category_list

urlpatterns = [
    path('add', add_food, name="add_food"),
    path('list', food_list, name="food_list"),
    path('categories/', category_list, name='category_list'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
]
