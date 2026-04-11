# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""
    return Product("Laptop", 200, 10)


# --- Testy z fixture ---

def test_is_available(product):
    """Sprawdz dostepnosc produktu."""
    assert product.is_available() == True


def test_total_value(product):
    """Sprawdz wartosc calkowita."""
    assert product.total_value() == 200 * 10
    pass


# --- Testy z parametryzacja ---

@pytest.mark.parametrize("amount, expected_quantity", [
     (5, 15),       # dodanie 5 do poczatkowych 10 = 15
     (0, 10),       # dodanie 0 = bez zmian
     (100, 110),    # dodanie 100
     (1,11)         # dodanie 1
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    """Testuje add_stock z roznymi wartosciami."""
    product.add_stock(amount)
    assert product.quantity == expected_quantity
    pass

@pytest.mark.parametrize("percent, expected_price", [
    (0, 200.0),
    (50, 100.0),
    (100, 0.0),
])

def test_apply_discount(product, percent, expected_price):
    product.apply_discount(percent)
    assert product.price == expected_price

# --- Testy bledow ---

def test_remove_stock_too_much_raises(product):
    """Sprawdz, czy proba usuniecia za duzej ilosci rzuca ValueError."""
    with pytest.raises(ValueError):
        product.remove_stock(11)
    pass


def test_add_stock_negative_raises(product):
    """Sprawdz, czy ujemna wartosc w add_stock rzuca ValueError."""
    with pytest.raises(ValueError):
        product.add_stock(-5)
    pass
