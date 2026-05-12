"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition():
    calc = Calculator()
    # Normal
    assert calc.addition(2, 3) == 5
    # Limite
    assert calc.addition(0, 0) == 0
    assert calc.addition(-1, 1) == 0
    # Erreur (Type)
    try:
        calc.addition("a", 1)
    except TypeError:
        assert True

def test_subtraction():
    calc = Calculator()
    # Normal
    assert calc.subtraction(10, 5) == 5
    # Limite
    assert calc.subtraction(0, 0) == 0
    assert calc.subtraction(5, 10) == -5

def test_multiplication():
    calc = Calculator()
    # Normal
    assert calc.multiplication(3, 4) == 12
    # Limite
    assert calc.multiplication(5, 0) == 0
    assert calc.multiplication(-2, 3) == -6

def test_division():
    calc = Calculator()
    # Normal
    assert calc.division(10, 2) == 5
    # Limite
    assert calc.division(0, 5) == 0
    # Erreur
    assert calc.division(10, 0) == "Erreur : division par zéro"
    assert calc.last_result == "Error"
    
