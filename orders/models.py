from django.db import models

#Added
class Pizzas(models.Model):
    style = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.style}'

# added - of note, delete 'small' duplicate entry
class Sizes(models.Model):
    size = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f'{self.size}'

# cheese = 0 toppings
# special = 4 toppings

class Pizza(models.Model):
    type = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    # set toppings to 0 if toppings are not specified
    toppings = models.IntegerField()
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    price = models.FloatField(max_length=4)

    def __str__(self):
        return f'Pizza type: {self.type}, Toppings {self.toppings}, Size = {self.size}, Price = {self.price}' 

class Toppings(models.Model):
    toppings = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.toppings}'

#how to add extra cheese to a sub? Add an optional boolean?

class Subs(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.type}'

class Sub(models.Model):
    type = models.ForeignKey(Subs, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    price = models.FloatField(max_length=4)
    # toppings = models.ManyToManyField(Toppings, blank=True)

    def __str__(self):
        return f'Type: {self.type}, Size = {self.size}, {self.price}'

    
class Pastas(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class PastaProtein(models.Model):
    protein = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.protein}'

class Pasta(models.Model):
    name = models.ForeignKey(Pastas, on_delete=models.CASCADE)
    price = price = models.FloatField(max_length=4)
    protein = models.ForeignKey(PastaProtein, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Protein: {self.protein}'


class Platters(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.type}'

class Platter(models.Model):
    name = models.ForeignKey(Platters, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    price = models.FloatField(max_length=4)

    def __str__(self):
        return f'Name: {self.name}, Size: {self.size}, Price: {self.price}'

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField(max_length=4)

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}'

