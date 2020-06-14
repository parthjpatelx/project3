from django.db import models

# Create your models here.
class Pizzas(models.Model):
    style = models.CharField(max_length=64)

    def __str(self):
        return f'{self.style}'

class Sizes(models.Model):
    size = models.CharField(max_length=64)

class Pizza(models.Model):
    type = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    # set toppings to 0 if toppings are not specified
    toppings_int = models.IntegerField()
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=4)

    def __str__(self):
        return f'Pizza type: {self.type}, Toppings {self.toppings_int}, Size = {self.size}, Price = {self.price}' 

class Toppings(models.Model):
    toppings = models.CharField(max_length=64)

class Subs(models.Model):
    type = models.CharField(max_length=64)

class Sub(models.Model):
    type = models.ForeignKey(Subs, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=4)
    toppings = models.ManyToManyField(Toppings, blank=True)

class Pasta(models.Model):
    name = models.ForeignKey(Pastas, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=4)
    protein = models.ForeignKey(PastaProtein, on_delete=models.CASCADE)

class PastaProtein(models.Model):
    name = models.CharField(max_length=64)

class Platter(models.Model):
    name = models.ForeignKey(Platters, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=4)

class Platters(models.Model):
    type = models.CharField(max_length=64)
