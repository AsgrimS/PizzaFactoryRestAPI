from rest_framework import serializers

from . import models


class PizzasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pizzas
        fields = [
            "name",
            "crust",
            "price",
        ]


class ToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Toppings
        fields = ["name", "created"]


class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drinks
        fields = [
            "name",
            "price",
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = [
            "created",
            "bill",
        ]


class CrustSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Crust
        fields = ["name"]
