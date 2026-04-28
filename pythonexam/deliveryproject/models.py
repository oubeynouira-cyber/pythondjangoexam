from django.db import models

# ======================
# FOURNISSEUR
# ======================
class Supplier(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='suppliers/', blank=True, null=True)

    def __str__(self):
        return self.nom


# ======================
# CLIENT
# ======================
class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


# ======================
# PRODUIT
# ======================
class Product(models.Model):
    nom = models.CharField(max_length=100)
    qte_stock = models.IntegerField()
    prix_achat = models.FloatField()
    prix_vente = models.FloatField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    fournisseur = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


# ======================
# LIVRAISON
# ======================
class Delivery(models.Model):
    STATUT_CHOICES = [
        ("En cours", "En cours"),
        ("Livré", "Livré"),
        ("Annulé", "Annulé"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_livraison = models.DateField()
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES, default="En cours")
    @property
    def total(self):
        return sum(item.total for item in self.deliveryitem_set.all())

    @property
    def profit(self):
        return sum(
            (item.produit.prix_vente - item.produit.prix_achat) * item.quantite
            for item in self.deliveryitem_set.all()
        )
    def __str__(self):
        return f"Livraison {self.id} - {self.client}"


# ======================
# DETAIL LIVRAISON (PRO)
# ======================
class DeliveryItem(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    produit = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.pk:  # updating existing item
            old = DeliveryItem.objects.get(pk=self.pk)
            diff = self.quantite - old.quantite
            self.produit.qte_stock -= diff
        else:  # new item
            self.produit.qte_stock -= self.quantite
        self.produit.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.produit.qte_stock += self.quantite
        self.produit.save()
        super().delete(*args, **kwargs)

    @property
    def total(self):
        return self.quantite * self.produit.prix_vente

    def __str__(self):
        return f"{self.produit} x {self.quantite}"