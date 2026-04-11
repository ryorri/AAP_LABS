# ========================================
# Szkielet pliku: product.py
# Uzupelnij implementacje!
# ========================================

class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # Pamietaj o walidacji: price >= 0, quantity >= 0
        if price < 0:
            raise ValueError("Cena nie moze byc ujemna!")
        if quantity < 0:
            raise ValueError("Ilosc nie moze byc ujemna!")
        self.name = name
        self.price = price
        self.quantity = quantity
        pass

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Ilosc do dodania nie moze byc ujemna!")
        self.quantity += amount

    def remove_stock(self, amount: int):
        if amount < 0 or amount > self.quantity:
            raise ValueError("Ilosc do usuniecia nie moze byc ujemna!")
        self.quantity -= amount

    def is_available(self) -> bool:
        return self.quantity > 0

    def total_value(self) -> float:
        return self.price * self.quantity
    
    def apply_discount(self, percent: float):
        """Obniza cene o podany procent (0-100)."""
        if percent < 0 or percent > 100:
            raise ValueError("Procent rabatu musi byc miedzy 0 a 100!")
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount