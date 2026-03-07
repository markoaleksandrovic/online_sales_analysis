class Cart:
    def __init__(self):
        self.cart_items = []
    
    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"{product.name} dodat u korpu!")
    
    def calculate_total(self):
        total = sum(p.price * p.quantity for p in self.cart_items)
        return total
    
    def display_cart(self):
        print("\n--- Sadržaj korpe ---")
        for item in self.cart_items:
            item.display_info()
        print(f"Ukupno za naplatu: {self.calculate_total()} RSD")
