"""
Ce module regroupe les fonctions arithmétiques utilisées par l’application Flask de la calculatrice.
Chaque fonction est documentée avec ses paramètres, sa valeur de retour et son comportement.
"""

def add(a,b):
    """
    Retourne la somme de a et b.

    Paramètres:
        a (float): Premier opérande
        b (float): Deuxième opérade

    Sortie:
        float: Somme de a et b
    """
    return a + b

def subtract(a,b):
    """
    Retourne la différence entre a et b.

    Paramètres:
        a (float): Premier opérande
        b (float): Deuxième opérade

    Sortie:
        float: Différence de a et b
    """
    return a - b

def multiply(a,b):
    """
    Retourne le produit de a et b.

    Paramètres:
        a (float): Premier opérande
        b (float): Deuxième opérade

    Sortie:
        float: Produit de a et b
    """
    return a * b

def divide(a,b):
    """
    Retourne la division entre a et b.

    Paramètres:
        a (float): Premier opérande
        b (float): Deuxième opérade

    Sortie:
        float: Division entre a et b
    """
    return a / b
