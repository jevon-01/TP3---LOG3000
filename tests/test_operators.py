"""
Tests unitaires du module operators.py.

Ce fichier vérifie le bon fonctionnement des fonctions arithmétiques définies dans operators.py:
l'addition, la soustraction, la multiplication et la division.

Les tests couvrent :
- les nombres positifs et négatifs
- les valeurs nulles
- les nombres décimaux
- les cas d’erreur

Ces tests garantissent une fiabilité des opérations utilisées par l’application de calculatrice.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from operators import add, subtract, multiply, divide

class TestAdd:
    """Tests unitaires pour l'addition du module operators.py"""
    def test_add_positive_numbers(self):
        """Teste l'addition de deux nombres positifs"""
        assert add(1, 2) == 3
        assert add(12, 20) == 32

    def test_add_negative_numbers(self):
        """Teste l'addition avec des nombres négatifs"""
        assert add(-9, -2) == -11
        assert add(-4, 7) == 3

    def test_add_zero(self):
        """Teste l'addition avec zéro"""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0

    def test_add_floats(self):
        """Teste l'addition de nombres décimaux"""
        assert add(0.5, 2.5) == 3.0
        
class TestSubtract:
    """Tests unitaires pour la soustraction du module operators.py"""
    def test_subtract_positive_numbers(self):
        """Teste la soustraction: subtract(a, b) = b - a"""
        assert subtract(5, 3) == 2
        assert subtract(11, 7) == 4

    def test_subtract_negative_numbers(self):
        """Teste la soustraction avec nombres négatifs"""
        assert subtract(-5, -3) == -2
        assert subtract(5, -3) == 8

    def test_subtract_zero(self):
        """Teste la soustraction avec zéro"""
        assert subtract(0, 5) == -5
        assert subtract(5, 0) == 5
        assert subtract(0, 0) == 0

    def test_subtract_floats(self):
        """Teste la soustraction de nombres décimaux"""
        assert subtract(3.5, 2.5) == 1.0

class TestMultiply:
    """Tests unitaires pour la multiplication du module operators.py"""
    def test_multiply_positive_numbers(self):
        """Teste la multiplication: multiply(a, b) = a * b"""
        assert multiply(4, 4) == 16
        assert multiply(3, 2) == 6

    def test_multiply_by_zero(self):
        """Teste la multiplication avec zéro"""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0

    def test_multiply_negative_exponent(self):
        """Teste la multiplication avec un négatif"""
        assert multiply(2, -1) == -2
        assert multiply(-3, 1) == -3
        assert multiply(-8, -2) == 16

    def test_multiply_floats(self):
        """Teste la multiplication avec décimaux"""
        assert multiply(4.0, 2.0) == 8.0

class TestDivide:
    """Tests unitaires pour la division du module operators.py"""
    def test_divide_positive_numbers(self):
        """Teste la division : divide(a, b) = a / b"""
        assert divide(8, 2) == 4

    def test_divide_negative_numbers(self):
        """Teste la division avec nombres négatifs"""
        assert divide(-8, 2) == -4

    def test_divide_zero_dividend(self):
        """Teste la division avec zéro au numérateur"""
        assert divide(0, 2) == 0

    def test_divide_zero_divisor(self):
        """Teste la division par zéro (doit lever une exception)"""
        with pytest.raises(ZeroDivisionError):
            divide(2, 0)

    def test_divide_remainder(self):
        """Teste la division avec décimales"""
        assert divide(5, 2) == 2.5  
