from rest_framework import serializers

from . import models


class PizzasSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pizzas
        fields = [
            "crust",
            "price",
            "created",
            "last_updated",
        ]

class ToppingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Toppings
        fields = [
            "name",
            "created",
            "last_updated",
        ]

class DrinksSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Drinks
        fields = [
            "price",
            "created",
            "last_updated",
            "name",
        ]

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = [
            "created",
            "bill",
            "last_updated",
        ]
