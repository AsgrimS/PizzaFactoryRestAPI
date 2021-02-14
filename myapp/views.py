from django.views import generic
from . import models
from . import forms


class PizzasListView(generic.ListView):
    model = models.Pizzas
    form_class = forms.PizzasForm


class PizzasCreateView(generic.CreateView):
    model = models.Pizzas
    form_class = forms.PizzasForm


class PizzasDetailView(generic.DetailView):
    model = models.Pizzas
    form_class = forms.PizzasForm


class PizzasUpdateView(generic.UpdateView):
    model = models.Pizzas
    form_class = forms.PizzasForm
    pk_url_kwarg = "pk"


class ToppingsListView(generic.ListView):
    model = models.Toppings
    form_class = forms.ToppingsForm


class ToppingsCreateView(generic.CreateView):
    model = models.Toppings
    form_class = forms.ToppingsForm


class ToppingsDetailView(generic.DetailView):
    model = models.Toppings
    form_class = forms.ToppingsForm


class ToppingsUpdateView(generic.UpdateView):
    model = models.Toppings
    form_class = forms.ToppingsForm
    pk_url_kwarg = "pk"


class DrinksListView(generic.ListView):
    model = models.Drinks
    form_class = forms.DrinksForm


class DrinksCreateView(generic.CreateView):
    model = models.Drinks
    form_class = forms.DrinksForm


class DrinksDetailView(generic.DetailView):
    model = models.Drinks
    form_class = forms.DrinksForm


class DrinksUpdateView(generic.UpdateView):
    model = models.Drinks
    form_class = forms.DrinksForm
    pk_url_kwarg = "pk"


class OrderListView(generic.ListView):
    model = models.Order
    form_class = forms.OrderForm


class OrderCreateView(generic.CreateView):
    model = models.Order
    form_class = forms.OrderForm


class OrderDetailView(generic.DetailView):
    model = models.Order
    form_class = forms.OrderForm


class OrderUpdateView(generic.UpdateView):
    model = models.Order
    form_class = forms.OrderForm
    pk_url_kwarg = "pk"
