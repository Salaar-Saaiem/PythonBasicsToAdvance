'''
2. Product Inventory

Create a class Product.

Attributes:
product_name
price
stock

Methods:
add_stock(quantity)
sell_product(quantity)
show_product()

Expected:
Product: Laptop
Price: ₹50000
Stock: 10

Sold 2 units
Remaining Stock: 8
''' 

class Product:
    def __init__(self, product_name, price, stock):
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def add_stock (self, quantity):
        print(f'Product Name: {self.product_name}')
        print(f'Product Price:',self.price)
        print(f'Product Stock:',self.stock)
        self.stock += quantity
        print(f'{quantity} stocks added')
        print(f'Remaining Stock - {self.stock} \n')

    def sell_product(self, quantity):
        print(f'Product Name: {self.product_name}')
        print(f'Product Price:',self.price)
        print(f'Product Stock:',self.stock)
        self.stock -= quantity
        print(f'{quantity} stocks sold')
        print(f'Remaining Stock - {self.stock} \n')
    
Laptop=Product('Laptop', 50000, 12)
Laptop.add_stock(5)
Laptop.sell_product(2)
