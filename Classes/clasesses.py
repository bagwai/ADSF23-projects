# Arewa Data Science Fellowship 2023
# Python Crash Course
# Chapter 9: Classes

#9.1

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Pizza House", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9.2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


restaurant1 = Restaurant("Pizza House", "Italian")
restaurant2 = Restaurant("Burger Joint", "American")
restaurant3 = Restaurant("Sushi Place", "Japanese")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#9.3
class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! How are you today?")


user1 = User("Babangida", "Sani", 25, "Kano", "Software Developer")
user2 = User("Mahmoud", "Ahmad", 20, "Kano", "Marketing Manager")
user3 = User("Auwal", "Idris", 40, "Kaduna", "Sales Representative")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

#9.4

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, num_customers):
        self.number_served = num_customers

    def increment_number_served(self, num_customers):
        self.number_served += num_customers

restaurant = Restaurant("Pizza House", "Italian")
print(f"Number of customers served: {restaurant.number_served}")
restaurant.number_served = 10
print(f"Number of customers served: {restaurant.number_served}")
restaurant.set_number_served(20)
print(f"Number of customers served: {restaurant.number_served}")
restaurant.increment_number_served(15)
print(f"Number of customers served: {restaurant.number_served}")


#9.5

class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! How are you today?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("John", "Doe", 25, "New York", "Software Developer")
print(f"Login attempts: {user.login_attempts}")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")

#9.6

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print("- " + flavor)

my_ice_cream_stand = IceCreamStand("The Ice Cream Shop", "ice cream")
my_ice_cream_stand.flavors = ["vanilla", "chocolate", "strawberry", "mint"]
my_ice_cream_stand.show_flavors()

