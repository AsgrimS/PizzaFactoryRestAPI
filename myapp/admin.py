from django.contrib import admin
from django import forms

from . import models


class PizzasAdminForm(forms.ModelForm):
    class Meta:
        model = models.Pizzas
        fields = "__all__"


class PizzasAdmin(admin.ModelAdmin):
    form = PizzasAdminForm
    list_display = [
        "crust",
        "price",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class ToppingsAdminForm(forms.ModelForm):
    class Meta:
        model = models.Toppings
        fields = "__all__"


class ToppingsAdmin(admin.ModelAdmin):
    form = ToppingsAdminForm
    list_display = [
        "name",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class DrinksAdminForm(forms.ModelForm):
    class Meta:
        model = models.Drinks
        fields = "__all__"


class DrinksAdmin(admin.ModelAdmin):
    form = DrinksAdminForm
    list_display = [
        "name",
        "price",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class OrderAdminForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = "__all__"


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = [
        "created",
        "bill",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "bill",
        "last_updated",
    ]


class CrustAdminForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = "__all__"


class CrustAdmin(admin.ModelAdmin):
    form = CrustAdminForm
    list_display = [
        "created",
        "name",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.Crust, CrustAdmin)
admin.site.register(models.Pizzas, PizzasAdmin)
admin.site.register(models.Toppings, ToppingsAdmin)
admin.site.register(models.Drinks, DrinksAdmin)
admin.site.register(models.Order, OrderAdmin)
