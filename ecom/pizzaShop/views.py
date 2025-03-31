from django.shortcuts import render, redirect
from django.forms import formset_factory

from django.contrib import messages

from .forms import *
from .models import *


# Create your views here.

def home(request):
    return render(request, 'pizzaShop/home.html', {})


def order(request):

    form = PizzaForm()
    multiple_form = MultiplePizzaForm()
    
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            order_id = created_pizza.order_id
            messages.success(request, (f"Thanks for ordering! Your {filled_form.cleaned_data['size']} {filled_form.cleaned_data['topping1']} & {filled_form.cleaned_data['topping2']} pizza in on its way!"))
    
        form = PizzaForm()
        pizza = Pizza.objects.get(order_id = order_id)
        return render(request, 'pizzaShop/order.html', {'pizzaform': form, 'multiple_form': multiple_form, 'order_id': order_id ,'pizza': pizza})


    return render(request, 'pizzaShop/order.html', {'pizzaform': form, 'multiple_form': multiple_form})




def orderpizzas(request):
    num_pizza = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)

    if filled_multiple_pizza_form.is_valid():
        num_pizza = filled_multiple_pizza_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra = num_pizza)
    formset = PizzaFormSet()

    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                messages.success(request, (f"Thanks for ordering! Your {form.cleaned_data['size']} {form.cleaned_data['topping1']} & {form.cleaned_data['topping2']} pizza in on its way!"))
        else:
            messages.error("Order was not created, Please try Again!")

        return redirect('orderpizzas')


    return render(request, 'pizzaShop/orderpizzas.html', {'formset': formset})



def edit_order(request, id):
    pizza = Pizza.objects.get(order_id = id)

    form = PizzaForm(instance=pizza)

    if request.method == "POST":
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, (f"Your order is updated for {filled_form.cleaned_data['size']} {filled_form.cleaned_data['topping1']} & {filled_form.cleaned_data['topping2']} pizza!"))

            form = filled_form
    
    return render(request, 'pizzaShop/edit_order.html', {'pizzaform': form, 'pizza': pizza})