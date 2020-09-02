from django.shortcuts import render


def index(request):
    return render(request, 'amyra/index.html')


def customers(request):
    return render(request, 'amyra/customers.html')