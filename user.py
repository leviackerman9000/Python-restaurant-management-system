from abc import ABC

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name 
        self.phone = phone 
        self.email = email
        self.address = address 


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
        self.menu = FoodItem()
        
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
        


mn = Menu()
item = FoodItem("Pizza", 12.45, 12)
mn.add_menu_item(item)
mn.show_menu()


