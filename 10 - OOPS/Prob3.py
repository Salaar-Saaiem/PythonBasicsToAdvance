'''
2. Car Class - Create a class Car.

Attributes:
brand
model
top_speed

Method:
show_details()

Create 3 car objects and display their details.
'''

# Creating Cars Blueprint [Class]
class Car:
    def __init__(self, Brand, Model, TopSpeed):
        self.brand = Brand
        self.model = Model
        self.topspeed = TopSpeed

    def details(self):
        print(f'\nBrand: {self.brand} \nModel: {self.model} \nTop Speed: {self.topspeed}')

# Creating Objects
tesla = Car('Tesla', 'Model S', 210)
renoult = Car('Renoult', 'Duster', 200)
mercedes = Car('Mercedes', 'Benz S4', 260)

tesla.details()
renoult.details()
mercedes.details()