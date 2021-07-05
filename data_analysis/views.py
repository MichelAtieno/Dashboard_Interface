from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.
@login_required()
def index(request):
    return render(request, "index.html")

@login_required()
def staff(request):
    return render(request, "staff.html")

@login_required()
def product(request):
    items = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm()

    context = {
        'items': items,
        'form': form
    }

    return render(request, "product.html", context)

def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('product')
    return render(request, "product_delete.html")

def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=="POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form':form
    }

    return render(request, "product_update.html", context)


@login_required()
def order(request):
    return render(request, "order.html")
