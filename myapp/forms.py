from django import forms
from . import models


class PizzasForm(forms.ModelForm):
    class Meta:
        model = models.Pizzas
        fields = [
            "crust",
            "price",
            "topings",
        ]


class ToppingsForm(forms.ModelForm):
    class Meta:
        model = models.Toppings
        fields = [
            "name",
        ]


class DrinksForm(forms.ModelForm):
    class Meta:
        model = models.Drinks
        fields = [
            "price",
            "name",
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            "bill",
            "drinks",
            "pizzas",
        ]
