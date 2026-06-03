from django.shortcuts import render, redirect
from menu.models import Category, Food
from menu.forms import FoodForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

def food_list(request):
    foods = Food.objects.all()
    context = {'foods':foods}
    return render(request, 'menu/index.html', context=context)

@staff_member_required
def add_food(request):
    form = FoodForm()
    if request.method == "POST":
        form = FoodForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "غذای جدید به منو اضافه شد")
            return redirect("food_list")
        else:
            messages.error(request, "خطایی در پر کردن اطلاعات وجود دارد")

    return render(request, 'menu/add_food.html', context={'form': form})
        