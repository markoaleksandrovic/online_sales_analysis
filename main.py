from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreiraj instancu ProductManager
manager = ProductManager()

# Dodaj proizvode
p1 = Product("Laptop", 50000, 10)
p2 = Product("Miš", 1500, 50)
p3 = Product("Tastatura", 3000, 30)
p4 = Product("Monitor", 25000, 15)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)

# Prikaz i ukupna vrednost
manager.display_all_products()
manager.calculate_total_value()
