from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Pizzas", api.PizzasViewSet)
router.register("Toppings", api.ToppingsViewSet)
router.register("Drinks", api.DrinksViewSet)
router.register("Order", api.OrderViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("myapp/Pizzas/", views.PizzasListView.as_view(), name="myapp_Pizzas_list"),
    path("myapp/Pizzas/create/", views.PizzasCreateView.as_view(), name="myapp_Pizzas_create"),
    path("myapp/Pizzas/detail/<int:pk>/", views.PizzasDetailView.as_view(), name="myapp_Pizzas_detail"),
    path("myapp/Pizzas/update/<int:pk>/", views.PizzasUpdateView.as_view(), name="myapp_Pizzas_update"),
    path("myapp/Toppings/", views.ToppingsListView.as_view(), name="myapp_Toppings_list"),
    path("myapp/Toppings/create/", views.ToppingsCreateView.as_view(), name="myapp_Toppings_create"),
    path("myapp/Toppings/detail/<int:pk>/", views.ToppingsDetailView.as_view(), name="myapp_Toppings_detail"),
    path("myapp/Toppings/update/<int:pk>/", views.ToppingsUpdateView.as_view(), name="myapp_Toppings_update"),
    path("myapp/Drinks/", views.DrinksListView.as_view(), name="myapp_Drinks_list"),
    path("myapp/Drinks/create/", views.DrinksCreateView.as_view(), name="myapp_Drinks_create"),
    path("myapp/Drinks/detail/<int:pk>/", views.DrinksDetailView.as_view(), name="myapp_Drinks_detail"),
    path("myapp/Drinks/update/<int:pk>/", views.DrinksUpdateView.as_view(), name="myapp_Drinks_update"),
    path("myapp/Order/", views.OrderListView.as_view(), name="myapp_Order_list"),
    path("myapp/Order/create/", views.OrderCreateView.as_view(), name="myapp_Order_create"),
    path("myapp/Order/detail/<int:pk>/", views.OrderDetailView.as_view(), name="myapp_Order_detail"),
    path("myapp/Order/update/<int:pk>/", views.OrderUpdateView.as_view(), name="myapp_Order_update"),
)
