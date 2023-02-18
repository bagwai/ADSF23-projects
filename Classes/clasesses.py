# Arewa Data Science Fellowship 2023
# Python Crash Course
# Chapter 9: Classes

import random
from admin import Admin

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


user = User("Mubarak", "Daha", 25, "Kano", "Software Developer")
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

#9.7 & 9.8

class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.city}.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Administrator {self.first_name} {self.last_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("The administrator has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()

admin = Admin("Mubarak", "Daha", 35, "Kano")
#admin.show_privileges()


#9.9

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize the car's attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Check the battery size and set the capacity to 100 if it isn't already."""
        if self.battery_size < 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

#9.11
my_admin = Admin("Mubarak", "Daha", "bagwai", "mubarak@email.com")
#my_admin.privileges.show_privileges()

#9.12


my_admin = Admin("Mubarak", "Daha", "bagwai", "mubarak@email.com")
my_admin.privileges.show_privileges()

#9.13

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        print(random.randint(1, self.sides))

six_sided_die = Die()
for i in range(10):
    six_sided_die.roll_die()

ten_sided_die = Die(sides=10)
for i in range(10):
    ten_sided_die.roll_die()

twenty_sided_die = Die(sides=20)
for i in range(10):
    twenty_sided_die.roll_die()

#9.14

lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_numbers = random.sample(lottery_numbers, 4)
print(f"The winning numbers are: {winning_numbers}")

#9.15

lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_numbers = random.sample(lottery_numbers, 4)

my_ticket = [3, 7, 'A', 'B']
iterations = 0

while True:
    iterations += 1
    random_ticket = random.sample(lottery_numbers, 4)
    if random_ticket == my_ticket:
        break
        
print(f"It took {iterations} iterations to match the winning ticket {winning_numbers}.")
