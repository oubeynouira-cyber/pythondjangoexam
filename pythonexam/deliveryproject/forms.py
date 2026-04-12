from django import forms
from .models import Delivery, DeliveryItem, Client, Product, Supplier

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryItemForm(forms.ModelForm):
    class Meta:
        model = DeliveryItem
        fields = '__all__'