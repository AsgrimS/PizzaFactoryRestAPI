import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from myapp import models as myapp_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_myapp_Pizzas(**kwargs):
    defaults = {}
    defaults["crust"] = ""
    defaults["price"] = ""
    if "topings" not in kwargs:
        defaults["topings"] = create_myapp_Toppings()
    defaults.update(**kwargs)
    return myapp_models.Pizzas.objects.create(**defaults)
def create_myapp_Toppings(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return myapp_models.Toppings.objects.create(**defaults)
def create_myapp_Drinks(**kwargs):
    defaults = {}
    defaults["price"] = ""
    defaults["name"] = ""
    defaults.update(**kwargs)
    return myapp_models.Drinks.objects.create(**defaults)
def create_myapp_Order(**kwargs):
    defaults = {}
    defaults["bill"] = ""
    if "drinks" not in kwargs:
        defaults["drinks"] = create_myapp_Drinks()
    if "pizzas" not in kwargs:
        defaults["pizzas"] = create_myapp_Pizzas()
    defaults.update(**kwargs)
    return myapp_models.Order.objects.create(**defaults)
