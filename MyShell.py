# important the order that we do this, helps us to see our database 

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django
django.setup()

from MainApp.models import Pizza, Topping

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id)
    print(pizza.text)
    print(pizza.date_added)

p = Pizza.objects.get(id=1)
print(p)

#bc there is a pk fk relationship, p topping is a fk to the pizza model
toppings = p.topping_set.all()

for t in toppings:
    print(t)