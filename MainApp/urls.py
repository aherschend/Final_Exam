from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'MainApp'

# '' keeps it as the blank page, we would like to change it to our own custom homepage
# the name of our view will be index so that is what we will also name our html file
urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
    path('new_comment/<int:pizza_id>/',views.new_comment, name='new_comment')
]

