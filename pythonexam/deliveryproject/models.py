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
    email = models.EmailField()

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

    def __str__(self):
        return f"Livraison {self.id} - {self.client}"


# ======================
# DETAIL LIVRAISON (PRO)
# ======================
class DeliveryItem(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    produit = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.produit} x {self.quantite}"