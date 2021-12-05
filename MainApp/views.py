from django.shortcuts import render

from .models import Pizza

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


