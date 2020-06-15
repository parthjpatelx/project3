from django.db import models

# Create your models here.

# Create your models here.
class Pizzas(models.Model):
    style = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.style}'

class Sizes(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.size}'

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

    def __str__(self):
        return f'{self.toppings}'

class Subs(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.type}'

class Sub(models.Model):
    type = models.ForeignKey(Subs, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=4)
    toppings = models.ManyToManyField(Toppings, blank=True)

    def __str__(self):
        return f'Type: {self.type}, Size = {self.size}, {self.price}, {self.toppings}'

class Pasta(models.Model):
    name = models.ForeignKey(Pastas, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=4)
    protein = models.ForeignKey(PastaProtein, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Protein: {self.protein}'

class Pastas(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'name: {self.name}'

class PastaProtein(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'Name: {self.name}'

class Platter(models.Model):
    name = models.ForeignKey(Platters, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=4)

    def __str__(self):
        return f'Name: {self.name}, Size: {self.size}, Price: {self.price}'

class Platters(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f'Type: {self.type}'