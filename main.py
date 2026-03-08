from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreiraj instancu ProductManager
manager = ProductManager()

# PROMENJENI proizvodi
p1 = Product("Gaming Laptop", 75000, 5)      
p2 = Product("Bežični miš", 2500, 25)       
p3 = Product("Mehanička tastatura", 5000, 20)
p4 = Product("4K Monitor", 35000, 8)         

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)


# Korpa
cart = Cart()
cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p4)

cart.display_cart()
