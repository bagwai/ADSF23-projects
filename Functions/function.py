# Arewa Data Science Fellowship 2023
# Python Crash Course
# Chapter 8: Functions
# Function Basics

#8.1
def display_message():
    print("In this chapter, I am learning about functions in Python!")
    
# Calling the function
display_message()

# 8.2
def favarite_book(title):
    print(f"One of my favorite books is {title}.")
    
# Calling the function
favarite_book("Alice in Wonderland")

#8.3 
def make_shirt(size, message):
    print(f"The shirt size is {size}, and the message is '{message}'.")
    
# Using positional arguments
make_shirt("M", "Hello World")

# Using keyword arguments
make_shirt(size="L", message="I'm a programmer")


#8.4
def make_shirt(size="L", message="I love Python"):
    print(f"The shirt size is {size}, and the message is '{message}'.")
    
# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt("M")

# Custom size and message
make_shirt("S", "Python is awesome!")


#8.5
def describe_city(city, country="USA"):
    print(f"{city} is in {country}.")
    
# Cities in USA
describe_city("New York")
describe_city("Los Angeles")

# City outside of USA
describe_city("Paris", "France")

#8.6 

def city_country(city, country):
    return f"{city}, {country}"
    
# Calling the function
print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan"))
print(city_country("Sydney", "Australia"))


#8.7

def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        "artist": artist_name,
        "title": album_title
    }
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album
    
# Calling the function
album1 = make_album("The Beatles", "Abbey Road")
album2 = make_album("Pink Floyd", "The Wall")
album3 = make_album("Led Zeppelin", "IV", 8)

# Printing the album dictionaries
print(album1)
print(album2)
print(album3)

#8.8

def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        "artist": artist_name,
        "title": album_title
    }
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album

while True:
    artist = input("Enter the artist name (type 'q' to quit): ")
    if artist == 'q':
        break
    title = input("Enter the album title (type 'q' to quit): ")
    if title == 'q':
        break
    album = make_album(artist, title)
    print(album)


#8.9

def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Hello there!", "How are you?", "What are you up to?"]
show_messages(messages)

#8.10

def send_messages(messages):
    sent_messages = []
    while messages:
        message = messages.pop(0)
        print(message)
        sent_messages.append(message)
    return sent_messages

messages = ["Hello there!", "How are you?", "What are you up to?"]
sent_messages = send_messages(messages)
print("\nSent Messages:")
for message in sent_messages:
    print(message)

#8.11

messages = ["Hello there!", "How are you?", "What are you up to?"]
sent_messages = send_messages(messages[:])

print("\nArchived Messages:")
for message in messages:
    print(message)

print("\nSent Messages:")
for message in sent_messages:
    print(message)


#8.12
def make_sandwich(*items):
#Make a sandwich with the given items.
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('roast beef', 'cheddar cheese', 'onion', 'mayo')
make_sandwich('peanut butter', 'jelly')

#8.13

def build_profile(first, last, **user_info):
#Build a dictionary containing everything we know about a user.
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
        return profile

user_profile = build_profile('John', 'Doe', location='USA', field='Engineering', age=30)
print(user_profile)

#8.14

def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        car[key] = value
        return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

#8.15

