from django.shortcuts import redirect, render
from .forms import ToppingForm
from .models import Pizza, Topping

# Create your views here.

def index(request):
    # get and post - don't forget
    # every view processes a request, it needs to know if it is a get or post request
    # based on that we can either write to or read from the database

    return render(request, 'MainApp/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    # we don't really need to order by the date added here but we can

    # create a dictionary with variables you are going to use in your template
    context = {'pizzas':pizzas}


    return render(request, 'MainApp/pizzas.html', context) #this will populate the data on the template to render it to the browser


def pizza(request,pizza_id):
    #just like we did in MyShell.py
    pizza = Pizza.objects.get(id=pizza_id)
    #FK can be accessed using '_set'
    toppings = pizza.topping_set.all()
    context = {'pizza':pizza, 'toppings': toppings}

    return render(request, 'MainApp/pizza.html', context)


def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)

        if form.is_valid():
            # when we call save(), we include the argument commit = False to tell Django to create
            # a new topping object and assign it to new_topping without saving it
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            form.save()
            return redirect('MainApp:pizza', pizza_id=pizza_id)

    context = {'form': form, 'pizza': pizza}
    return render(request, 'MainApp/new_topping.html', context)



    



