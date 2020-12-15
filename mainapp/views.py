from django.shortcuts import render
from django.utils import timezone
from mainapp.models import ProductCategory, Product



def index(request):

    context = {
        'title': 'geek shop',

        'date': timezone.now()

    }

    return render(request, 'mainapp/index.html', context)


def products(request):

    context = {
        'title': 'geek shop - каталог',

        'currency': 'руб.',

        'products': Product.objects.all(),

        'categories': ProductCategory.objects.all()
    }


    return render(request, 'mainapp/products.html', context)
  
