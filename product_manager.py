from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        print(f"Proizvod {product.name} dodat!")
    
    def display_all_products(self):
        print("\n--- Svi proizvodi ---")
        for product in self.products:
            product.display_info()
    
    def calculate_total_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        print(f"\nUkupna vrednost inventara: {total} RSD")
        return total
def remove_product(self, product_name):
    for product in self.products:
        if product.name == product_name:
            self.products.remove(product)
            print(f"Proizvod {product_name} uklonjen!")
            return
    print(f"Proizvod {product_name} nije pronađen!")
