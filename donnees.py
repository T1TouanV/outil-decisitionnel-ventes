import calendar
import random


PRODUITS = ["Ordinateur", "Écran", "Clavier", "Souris"]
REGIONS = ["Normandie", "Bretagne", "Île-de-France", "Pays de la Loire"]


def generer_ventes(nb_ventes=100, annee=2026):
    """
    Génère aléatoirement des données de ventes.

    Chaque vente contient :
    - un mois ;
    - une région ;
    - un produit ;
    - une quantité vendue ;
    - un prix unitaire.

    Paramètres
    ----------
    nb_ventes : int
        Nombre de ventes à générer.
    annee : int
        Année associée aux ventes.

    Retour
    ------
    list[dict]
        Liste contenant les ventes générées.
    """
    ventes = []

    for _ in range(nb_ventes):
        numero_mois = random.randint(1, 12)

        vente = {
            "annee": annee,
            "mois": calendar.month_name[numero_mois],
            "numero_mois": numero_mois,
            "region": random.choice(REGIONS),
            "produit": random.choice(PRODUITS),
            "quantite": random.randint(1, 20),
            "prix_unitaire": random.randint(20, 1000),
        }

        ventes.append(vente)

    return ventes


def calculer_montant_vente(vente):
    """
    Calcule le montant d'une vente.

    Le montant correspond à :

        quantité × prix unitaire

    Paramètres
    ----------
    vente : dict
        Vente à analyser.

    Retour
    ------
    float
        Montant de la vente.
    """
    return vente["quantite"] * vente["prix_unitaire"]


def afficher_echantillon(ventes, n=5):
    """
    Affiche les n premières ventes.

    Paramètres
    ----------
    ventes : list[dict]
        Liste des ventes.
    n : int
        Nombre de ventes à afficher.
    """
    for vente in ventes[:n]:
        print(vente)
       