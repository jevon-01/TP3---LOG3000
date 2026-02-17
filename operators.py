"""
Ce module regroupe les fonctions arithmétiques utilisées par l’application Flask de la calculatrice.
Les docstrings et commentaires décrivent le rôle de chaque fonction, leurs paramètres d’entrée,
leurs valeurs de retour ainsi que les comportements spécifiques hérités de l’implémentation originale.
"""

def add(a,b):
    """
    Retourne la somme de a et b.

    Paramètres:
    : a (float): Premier opérande
    : b (float): Deuxième opérade

    Returns:
    : float: la somme de a et b
    """
    return a + b

def subtract(a,b):
    """
    Retourne la différence entre a et b.

    Paramètres:
    - a (float): Premier opérande
    - b (float): Deuxième opérade

    Returns:
    - float: la différence de a et b
    """
    return a - b

def multiply(a,b):
    """
    Retourne le produit de a et b.

    Paramètres:
    : a (float): Premier opérande
    : b (float): Deuxième opérade

    Returns:
    : float: le produit de a et b
    """
    return a * b

def divide(a,b):
    """
    Retourne la division entre a et b.

    Paramètres:
    : a (float): Premier opérande
    : b (float): Deuxième opérade

    Returns:
    : float: la division entre a et b
    """
    return a / b
