import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Pizzas_list_view():
    instance1 = test_helpers.create_myapp_Pizzas()
    instance2 = test_helpers.create_myapp_Pizzas()
    client = Client()
    url = reverse("myapp_Pizzas_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Pizzas_create_view():
    topings = test_helpers.create_myapp_Toppings()
    client = Client()
    url = reverse("myapp_Pizzas_create")
    data = {
        "crust": "text",
        "price": 1.0f,
        "topings": topings.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Pizzas_detail_view():
    client = Client()
    instance = test_helpers.create_myapp_Pizzas()
    url = reverse("myapp_Pizzas_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Pizzas_update_view():
    topings = test_helpers.create_myapp_Toppings()
    client = Client()
    instance = test_helpers.create_myapp_Pizzas()
    url = reverse("myapp_Pizzas_update", args=[instance.pk, ])
    data = {
        "crust": "text",
        "price": 1.0f,
        "topings": topings.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Toppings_list_view():
    instance1 = test_helpers.create_myapp_Toppings()
    instance2 = test_helpers.create_myapp_Toppings()
    client = Client()
    url = reverse("myapp_Toppings_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Toppings_create_view():
    client = Client()
    url = reverse("myapp_Toppings_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Toppings_detail_view():
    client = Client()
    instance = test_helpers.create_myapp_Toppings()
    url = reverse("myapp_Toppings_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Toppings_update_view():
    client = Client()
    instance = test_helpers.create_myapp_Toppings()
    url = reverse("myapp_Toppings_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Drinks_list_view():
    instance1 = test_helpers.create_myapp_Drinks()
    instance2 = test_helpers.create_myapp_Drinks()
    client = Client()
    url = reverse("myapp_Drinks_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Drinks_create_view():
    client = Client()
    url = reverse("myapp_Drinks_create")
    data = {
        "price": 1.0f,
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Drinks_detail_view():
    client = Client()
    instance = test_helpers.create_myapp_Drinks()
    url = reverse("myapp_Drinks_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Drinks_update_view():
    client = Client()
    instance = test_helpers.create_myapp_Drinks()
    url = reverse("myapp_Drinks_update", args=[instance.pk, ])
    data = {
        "price": 1.0f,
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_list_view():
    instance1 = test_helpers.create_myapp_Order()
    instance2 = test_helpers.create_myapp_Order()
    client = Client()
    url = reverse("myapp_Order_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Order_create_view():
    drinks = test_helpers.create_myapp_Drinks()
    pizzas = test_helpers.create_myapp_Pizzas()
    client = Client()
    url = reverse("myapp_Order_create")
    data = {
        "bill": 1.0f,
        "drinks": drinks.pk,
        "pizzas": pizzas.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_detail_view():
    client = Client()
    instance = test_helpers.create_myapp_Order()
    url = reverse("myapp_Order_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Order_update_view():
    drinks = test_helpers.create_myapp_Drinks()
    pizzas = test_helpers.create_myapp_Pizzas()
    client = Client()
    instance = test_helpers.create_myapp_Order()
    url = reverse("myapp_Order_update", args=[instance.pk, ])
    data = {
        "bill": 1.0f,
        "drinks": drinks.pk,
        "pizzas": pizzas.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
