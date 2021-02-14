from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PizzasViewSet(viewsets.ModelViewSet):
    """ViewSet for the Pizzas class"""

    queryset = models.Pizzas.objects.all()
    serializer_class = serializers.PizzasSerializer
    permission_classes = [permissions.IsAuthenticated]


class ToppingsViewSet(viewsets.ModelViewSet):
    """ViewSet for the Toppings class"""

    queryset = models.Toppings.objects.all()
    serializer_class = serializers.ToppingsSerializer
    permission_classes = [permissions.IsAuthenticated]


class DrinksViewSet(viewsets.ModelViewSet):
    """ViewSet for the Drinks class"""

    queryset = models.Drinks.objects.all()
    serializer_class = serializers.DrinksSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet for the Order class"""

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
