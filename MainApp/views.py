from django.shortcuts import render

# Create your views here.

def index(request):
    # get and post - don't forget
    # every view processes a request, it needs to know if it is a get or post request
    # based on that we can either write to or read from the database

    return render(request, 'MainApp/index.html')
