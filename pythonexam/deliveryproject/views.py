from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Client,Delivery,Supplier,Product
from .forms import ClientForm,DeliveryForm,DeliveryItemFormSet,SupplierForm,ProductForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
# HOME
def delivery_homepage(request):
    suppliers = Supplier.objects.all()
    return render(request, 'homepage/homepage.html', {
        'suppliers': suppliers
    })

#region AUTH
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('delivery_list')  
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists")
            return redirect('signup')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        return redirect('login')

    return render(request, 'auth/signup.html')
#endregion

#region delivery 

# LIST
@login_required(login_url='login')
def delivery_list(request):
    q = request.GET.get('q', '')
    deliveries = Delivery.objects.all().order_by('id')

    if q:
        deliveries = deliveries.filter(
            Q(statut__icontains=q) |
            Q(client__nom__icontains=q) |
            Q(date_livraison__icontains=q)
        )

    paginator = Paginator(deliveries, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'delivery/list.html', {
        'deliveries': page_obj,
        'q': q
    })

# CREATE 
@login_required(login_url='login')
def delivery_create(request):
    form = DeliveryForm(request.POST or None)
    formset = DeliveryItemFormSet(request.POST or None)  

    if form.is_valid() and formset.is_valid():  
        delivery = form.save()
        formset.instance = delivery  
        formset.save()  
        return redirect('delivery_list')

    return render(request, 'delivery/add.html', {
        'form': form,
        'formset': formset,  
    })


# UPDATE
@login_required(login_url='login')
def delivery_update(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    form = DeliveryForm(request.POST or None, instance=delivery)
    formset = DeliveryItemFormSet(request.POST or None, instance=delivery)  

    if form.is_valid() and formset.is_valid():  
        form.save()
        formset.save()  
        return redirect('delivery_list')

    return render(request, 'delivery/form.html', {
        'form': form,
        'formset': formset,  
    })


# DELETE 
@login_required(login_url='login')
def delivery_delete(request, id):
    delivery = get_object_or_404(Delivery, id=id)

    if request.method == "POST":
        delivery.delete()
        return redirect('delivery_list')

    return render(request, 'delivery/delete.html', {
        'delivery': delivery
    })


#details 
@login_required(login_url='login')
def delivery_detail(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    items = delivery.deliveryitem_set.all()
    return render(request, 'delivery/detail.html', {
        'delivery': delivery,
        'items': items,
    })
@login_required(login_url='login')
def delivery_mark_delivered(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    delivery.statut = "Livré"
    delivery.save()
    return redirect('delivery_list')
#endregion 

#region supplier   
# LIST
@login_required(login_url='login')
def supplier_list(request):
    q = request.GET.get('q', '')
    suppliers = Supplier.objects.all().order_by('id')
    
    if q:
        suppliers = suppliers.filter(
            Q(nom__icontains=q) |
            Q(email__icontains=q) |
            Q(adresse__icontains=q) |
            Q(telephone__icontains=q)
        )
    
    paginator = Paginator(suppliers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'supplier/list.html', {
        'suppliers': page_obj,
        'q': q
    })
#CREATE
@login_required(login_url='login')
def supplier_create(request):
    form = SupplierForm(request.POST or None, request.FILES or None)  # ✅ add request.FILES

    if form.is_valid():
        form.save()
        return redirect('supplier_list')

    return render(request, 'supplier/add.html', {
        'form': form
    })

# UPDATE
@login_required(login_url='login')
def supplier_update(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    form = SupplierForm(request.POST or None, request.FILES or None, instance=supplier)  # ✅ add request.FILES

    if form.is_valid():
        form.save()
        return redirect('supplier_list')

    return render(request, 'supplier/form.html', {
        'form': form
    })

# DELETE
@login_required(login_url='login')
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
@login_required(login_url='login')
def product_list(request):
    q = request.GET.get('q', '')
    products = Product.objects.all().order_by('id')

    if q:
        filters = Q(nom__icontains=q) | Q(fournisseur__nom__icontains=q)

        try:
            q_num = float(q)
            filters |= Q(prix_achat=q_num) | Q(prix_vente=q_num) | Q(qte_stock=q_num)
        except ValueError:
            pass

        products = products.filter(filters)

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product/list.html', {
        'products': page_obj,
        'q': q
    })

# CREATE
@login_required(login_url='login')
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)  # hedhy lel request.FILES

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'product/add.html', {
        'form': form
    })

# UPDATE
@login_required(login_url='login')
def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)  # hedhy lel request.FILES

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'product/form.html', {
        'form': form
    })

# DELETE
@login_required(login_url='login')
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
#Liste 
@login_required(login_url='login')
def client_list(request):
    q = request.GET.get('q', '')
    clients = Client.objects.all().order_by('id')

    if q:
        clients = clients.filter(
            Q(nom__icontains=q) |
            Q(prenom__icontains=q) |
            Q(email__icontains=q) |
            Q(telephone__icontains=q) |
            Q(adresse__icontains=q)
        )

    paginator = Paginator(clients, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'client/list.html', {
        'clients': page_obj,
        'q': q
    })
# CREATE
@login_required(login_url='login')
def client_create(request):
    form = ClientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('client_list')

    return render(request, 'client/add.html', {
        'form': form
    })

# UPDATE
@login_required(login_url='login')
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
@login_required(login_url='login')
def client_delete(request, id):
    client = get_object_or_404(Client, id=id)

    if request.method == "POST":
        client.delete()
        return redirect('client_list')

    return render(request, 'client/delete.html', {
        'client': client
    })

#endregion 

