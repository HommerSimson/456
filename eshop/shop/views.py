from django.shortcuts import render
from django import template
from django import templatetags
register = template.Library()

# Create your views here.
products = [
    {'name': 'Lenovo', 'price': '500', 'img': ['lenovo.jpg', 'lenovo2.jpg'], 'discount': True},
    {'name': 'Acer', 'price': '600', 'img': 'acer.jpg'},
    {'name': 'Asus', 'price': '700', 'img': 'asus.jpg'},
    {'name': 'Samsung', 'price': '900', 'img': 'samsung.jpeg'},
    {'name': 'HP', 'price': '700', 'img': 'HP.jpg'},
    {'name': 'Oracl', 'price': '700', 'img': 'Oracl.jpg'},
]


def startpage(request):
    context = {'products': products}
    return render(
        request,
        'index.html',
       context
      )

def product(request, name,):
    prod = {}

    for the_prod in products:
        if the_prod['name'].lower() == name.lower():
            prod = the_prod

            # s = list(filter(lambda prod: prod['name'] == name, products))
    # if len(s) > 0:
    #     prod = s[0]

    context = {'product': prod}
    return render(
        request,
        'tool1.html',
        context
      )
