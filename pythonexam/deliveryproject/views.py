from django.shortcuts import render, redirect, get_object_or_404
from .models import Client,Delivery,Supplier,Product
from .forms import ClientForm,DeliveryForm,SupplierForm,ProductForm


# HOME
def delivery_homepage(request):
    return render(request, 'homepage/homepage.html')




#region delivery 

# LIST
def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery/list.html', {
        'deliveries': deliveries
    })


# CREATE (RENAMED to match URL)
def delivery_create(request):
    form = DeliveryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('delivery_list')

    return render(request, 'delivery/add.html', {
        'form': form
    })


# UPDATE
def delivery_update(request, id):
    delivery = get_object_or_404(Delivery, id=id)

    form = DeliveryForm(request.POST or None, instance=delivery)

    if form.is_valid():
        form.save()
        return redirect('delivery_list')

    return render(request, 'delivery/form.html', {
        'form': form
    })


# DELETE (BETTER VERSION)
def delivery_delete(request, id):
    delivery = get_object_or_404(Delivery, id=id)

    if request.method == "POST":
        delivery.delete()
        return redirect('delivery_list')

    return render(request, 'delivery/delete.html', {
        'delivery': delivery
    })
#endregion 

#region supplier   
# LIST
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier/list.html', {
        'suppliers': suppliers
    })


# CREATE
def supplier_create(request):
    form = SupplierForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('supplier_list')

    return render(request, 'supplier/add.html', {
        'form': form
    })


# UPDATE
def supplier_update(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    form = SupplierForm(request.POST or None, instance=supplier)

    if form.is_valid():
        form.save()
        return redirect('supplier_list')

    return render(request, 'supplier/form.html', {
        'form': form
    })


# DELETE
def supplier_delete(request, id):
    supplier = get_object_or_404(Supplier, id=id)

    if request.method == "POST":
        supplier.delete()
        return redirect('supplier_list')

    return render(request, 'supplier/delete.html', {
        'supplier': supplier
    })

#endregion 

#region product 
# LIST
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {
        'products': products
    })

# CREATE
def product_create(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'product/add.html', {
        'form': form
    })

# UPDATE
def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'product/form.html', {
        'form': form
    })

# DELETE
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    return render(request, 'product/delete.html', {
        'product': product
    })

#endregion

#region client 

# LIST
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/list.html', {
        'clients': clients
    })

# CREATE
def client_create(request):
    form = ClientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('client_list')

    return render(request, 'client/add.html', {
        'form': form
    })

# UPDATE
def client_update(request, id):
    client = get_object_or_404(Client, id=id)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('client_list')

    return render(request, 'client/form.html', {
        'form': form
    })

# DELETE
def client_delete(request, id):
    client = get_object_or_404(Client, id=id)

    if request.method == "POST":
        client.delete()
        return redirect('client_list')

    return render(request, 'client/delete.html', {
        'client': client
    })

#endregion 

