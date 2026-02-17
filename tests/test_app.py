"""
Tests unitaires pour l'application Flask de la calculatrice.

Ce module teste :
- la fonction calculate()
- les différents cas d'erreur
- les routes HTTP GET et POST
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from app import app, calculate


def test_calculate_addition():
    """Teste une addition simple"""
    result = calculate("5 + 3")
    assert result == 8
    
def test_calculate_negative_number():
    """Teste un nombre négatif"""
    result = calculate("-5 + 3")
    assert result == -2

def test_calculate_subtraction():
    """Teste une soustraction"""
    result = calculate("5 - 3")
    assert result == 2


def test_calculate_multiplication():
    """Teste une multiplication"""
    result = calculate("2 * 3")
    assert result == 6


def test_calculate_division():
    """Teste une division"""
    result = calculate("5 / 2")
    assert result == 2.5


def test_calculate_empty():
    """Teste qu'une expression vide lève une erreur"""
    with pytest.raises(ValueError):
        calculate("")


def test_calculate_invalid_operands():
    """Teste qu'une expression avec opérandes invalides lève une erreur"""
    with pytest.raises(ValueError):
        calculate("abc + 5")


def test_index_get():
    """Teste la route GET /"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'display' in response.data


def test_index_post():
    """Teste la route POST / avec un calcul valide"""
    with app.test_client() as client:
        response = client.post('/', data={'display': '5+3'})
        assert response.status_code == 200
        assert b'8' in response.data

