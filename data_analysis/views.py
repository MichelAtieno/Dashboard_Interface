from django.shortcuts import render, redirect
from .models import Product, Order
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User

# Create your views here.
@login_required()
def index(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('index')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form': form,
    }
    return render(request, "index.html", context)

@login_required()
def staff(request):
    employees = User.objects.all()
    context= {
        'employees': employees
    }
    return render(request, "staff.html", context)

@login_required()
def staff_detail(request, pk):
    employees = User.objects.get(id=pk)
    context = {
        "employees": employees
    }
    return render(request, 'staff_detail.html', context)


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

@login_required()
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('product')
    return render(request, "product_delete.html")

@login_required()
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
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, "order.html", context)
