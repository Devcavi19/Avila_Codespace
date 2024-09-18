# Product Class: name, price
class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

p1 = Product("Fried Chicken", 68)
p2 = Product("Liempo", 330)
p3 = Product("Crispy Pata", 645)
p4 = Product("Litson Baka", 420)
p5 = Product("Litson Manok", 320)

# ShoppingCart Class
class ShoppingCart:
    
    # balance attribute is user's available balance
    def __init__(self, balance, products):
        self.balance = balance
        self.products = products
        
    # Methods: Add, list, and purchase product.
    def add_product(self, product):
        self.products.append(product)
        # self.balance -= product.price
    
    def list_products(self):
        for product in self.products:
            print(product.name)
        
    def purchase_product(self, index):
        if self.balance >= self.products[index].price:
            self.balance -= self.products[index].price
            print(f"Purchased {self.products[index].name} for ${self.products[index].price}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient balance.")
    
cart = ShoppingCart(2000, [])

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.add_product(p4)
cart.add_product(p5)

for product in cart.products:
    print(f"Added product: {product.name} (${product.price})")

print("\nProducts in cart:")
n = 1
for product in cart.products:
    print(f"{n}. {product.name} - ${product.price}")
    n += 1
print(f"Current balance: ${cart.balance}\n")

cart.purchase_product(0)
cart.purchase_product(1)
cart.purchase_product(2)
cart.purchase_product(3)
cart.purchase_product(4)