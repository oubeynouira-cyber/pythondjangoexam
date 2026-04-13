from django import forms
from .models import Delivery, DeliveryItem

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


class DeliveryItemForm(forms.ModelForm):
    class Meta:
        model = DeliveryItem
        fields = '__all__'