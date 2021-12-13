from django.db import models

# Create your models here.

class Pizza(models.Model):
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')

    # str method allows us to say whatever it is we want to say without it just putting
    # the type of object

    def __str__(self):
        return self.text #on the web page this shows us the actual text OF the object so it's important

class Topping(models.Model):
    # create a FK relationship to the Pizza model to relate to the pizza under toppings
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."

class Image(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images')

    def __str__(self):
        return self.text





