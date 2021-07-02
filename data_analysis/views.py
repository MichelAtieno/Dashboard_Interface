from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def index(request):
    return render(request, "index.html")

@login_required()
def staff(request):
    return render(request, "staff.html")

@login_required()
def product(request):
    return render(request, "product.html")



@login_required()
def order(request):
    return render(request, "order.html")
