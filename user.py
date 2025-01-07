from abc import ABC

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name 
        self.phone = phone 
        self.email = email
        self.address = address 

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        # check if item exists in item
        if item:    
            if quantity > item.quantity:
                print("Item quantity exceeded !")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added")         
        else:
            print("Item not found")

    def view_cart(self):
        print("**View Cart**")
        print("Name\tPrice\tQuantity")
        # items function brings the item and quantity in pairs
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{item.quantity}")
        print(f"Total Price : {self.cart.total_price}")

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity #in case already in the cart,increase quantity
        else:
            self.items[item] = item.quantity #newly added, so keep the quantity given by customer
    
    def remove(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())

    def clear(self):
        self.items = {}


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, phone, email, address)     
        self.age = age
        self.salary = salary
        self.designation = designation

# emp = Employee("rahim", "rahim@gmail.com", 1279787, "Dhaka", 23, "Chef", 12000)
# print(emp.age)
# print(emp.name)

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee) 

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)
    
    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []  # database
        self.menu = Menu()
        
    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List:")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address) # what to show in employee list


class Menu:
    def __init__(self):
        self.items = [] # items er database

    def add_menu_item(self,item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item deleted")
        else:
            print("Item not found")

    def show_menu(self):
        print("****MENU****")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        

mamar_res = Restaurant("Mamar Restaurant")
mn = Menu()
item = FoodItem("Pizza", 12.45, 12)
item2 = FoodItem("Burger", 10, 30)
admin = Admin("Rahim", "rahim@gmail.com", 1818566, "Sylhet")

admin.add_new_item(mamar_res, item)
admin.add_new_item(mamar_res, item2)


customer1 = Customer("Rahim", "rahim@gmail.com", 1818566, "Sylhet")
customer1.view_menu(mamar_res)

item_name = input("Enter item name: ")
item_quantity = int(input("Enter item quantity: "))

customer1.add_to_cart(mamar_res, item_name, item_quantity)
customer1.view_cart()
