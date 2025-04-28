class Car:
    def __init__(self, make, model, price, quantity):
        self.make = make
        self.model = model
        self.price = price
        self.quantity = quantity
        
    def sell(self):
        if self.quantity > 0:
            return True
            self.quantity = self.quantity - 1
        else:
            return False

class Customer:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Dealership:
    def __init__(self):
        self.cars = [] 
        self.customers = [] 

    def add_car(self, car):
        self.cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)

    def make_sale(self, car, customer):
        if car in self.cars and car.sell():
            
            print(f"{car.make} {car.model} sold to {customer.name} for ${car.price}    (customer ID = {customer.id})")
        else:
            print(f"Sorry, {car.make} {car.model} is not available or out of stock.")

    def display_inventory(self):
        print("Inventory:")
        for car in self.cars:
            print(f"{car.make} {car.model} - ${car.price} (Quantity: {car.quantity})")

dealership = Dealership()

car1 = Car("Toyota", "Camry", 20000, 0)  # 5 cars available
car2 = Car("Honda", "Civic", 18000, 3)   # 3 cars available

dealership.add_car(car1)
dealership.add_car(car2)

customer1 = Customer("John Doe" , 1233)
customer2 = Customer("Jane Doe" , 1256)
customer3 = Customer("Jhon xena" , 1216)

dealership.add_customer(customer1)
dealership.add_customer(customer2)
dealership.add_customer(customer3)

dealership.display_inventory()

dealership.make_sale(car1, customer1)  
dealership.make_sale(car2, customer2) 
dealership.make_sale(car2, customer3)  

dealership.display_inventory()
