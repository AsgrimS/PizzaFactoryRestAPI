from django.db import models
from django.urls import reverse


class Crust(models.Model):

    # Fields
    name = models.CharField(max_length=30, editable=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Pizzas(models.Model):

    # Relationships
    topings = models.ManyToManyField("myapp.Toppings", verbose_name="topings")
    crust = models.ForeignKey(Crust, on_delete=models.PROTECT)

    # Fields
    name = models.CharField(max_length=30, editable=True)
    price = models.FloatField(editable=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("myapp_Pizzas_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_Pizzas_update", args=(self.pk,))


class Toppings(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("myapp_Toppings_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_Toppings_update", args=(self.pk,))


class Drinks(models.Model):

    # Fields
    price = models.FloatField(editable=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("myapp_Drinks_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_Drinks_update", args=(self.pk,))


class Order(models.Model):

    # Relationships
    drinks = models.ManyToManyField("myapp.Drinks")
    pizzas = models.ManyToManyField("myapp.Pizzas")

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    bill = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("myapp_Order_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_Order_update", args=(self.pk,))
