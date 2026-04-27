from django import forms
from .models import Delivery, DeliveryItem,Client,Supplier,Product

#region DeliveryItems

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'
        widgets = {
            'date_livraison': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
            'statut': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'client': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].label = 'Client'
        self.fields['date_livraison'].label = 'Date de livraison'
        self.fields['statut'].label = 'Statut'

#endregion
#region deliveryitems
class DeliveryItemForm(forms.ModelForm):
    class Meta:
        model = DeliveryItem
        fields = '__all__'
       
#endregion 
#region Suppliers


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

#endregion
#region Clients
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
#endregion
#region Products
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'qte_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_achat': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'prix_vente': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fournisseur': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
#endregion


