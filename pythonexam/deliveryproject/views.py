from django.shortcuts import render, redirect, get_object_or_404
from .models import Delivery
from .forms import DeliveryForm
 
# HOME PAGE 
def delivery_homepage(request):
    return render(request, 'homepage/homepage.html')
 

# LIST
def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery/list.html', {'deliveries': deliveries})
 

# LIST
def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery/list.html', {'deliveries': deliveries})


# CREATE
def delivery_create(request):
    form = DeliveryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('delivery_list')
    return render(request, 'delivery/form.html', {'form': form})


# UPDATE
def delivery_update(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    form = DeliveryForm(request.POST or None, instance=delivery)
    if form.is_valid():
        form.save()
        return redirect('delivery_list')
    return render(request, 'delivery/form.html', {'form': form})


# DELETE
def delivery_delete(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    delivery.delete()
    return redirect('delivery_list')