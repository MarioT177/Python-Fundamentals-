# 1 8-3: T-shirt

def make_shirt(size, message):

    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt('small', 'Python fundamentals')
make_shirt(message="Cloud computing", size='medium')


# 8-4: Large T-shirts

def make_shirt(size='large', message='I love Python!'):

    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Python is hard')

# 8-5: Cities

def describe_city(city, country='mexico'):

    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('mexico city')
describe_city('reykjavik', 'iceland')
describe_city('Juarez')


# 2  8-9: Messages

def show_messages(messages):

    for message in messages:
        print(message)

messages = ["hello", "whats your name?"]
show_messages(messages)


# 8-10: Sending Messages

def show_messages(messages):

    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):

    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello", "whats your name?"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)

# 8-11 Archived Messages:

def show_messages(messages):

    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):

    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello", "whats your name?", ]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)


# 3 9-1 Restaurant


class Restaurant():


    def __init__(self, name, cuisine_type):

        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        msg = f"{self.name} serves {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):

        msg = f"{self.name} is open."
        print(f"\n{msg}")

restaurant = Restaurant('red robin', 'burgers')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2: Three restaurants


class Restaurant():


    def __init__(self, name, cuisine_type):

        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        msg = f"{self.name} serves {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):

        msg = f"{self.name} is open."
        print(f"\n{msg}")

red_robin = Restaurant('red robin', 'burgers')
red_robin.describe_restaurant()

chickennpickle = Restaurant("chicken n pickle", 'american food')
chickennpickle.describe_restaurant()

abuelos = Restaurant('abuelos', 'mexican food')
abuelos.describe_restaurant()

# 9-3: Users

class User():


    def __init__(self, first_name, last_name, username, email, location):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):

        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):

        print(f"\nWelcome back, {self.username}!")

mario = User('mario', 'trujillo', 'mario_t17', 'mario_t17@example.com', 'kansas')
mario.describe_user()
mario.greet_user()

antonio = User('antonio', 'trujillo', 'antoniotrujillo', '', 'kansas')
antonio.describe_user()
antonio.greet_user()


# 9-4: Number Saved


class Restaurant():


    def __init__(self, name, cuisine_type):

        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):

        msg = f"{self.name} serves {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):

        msg = f"{self.name} is open."
        print(f"\n{msg}")

    def set_number_served(self, number_served):

        self.number_served = number_served

    def increment_number_served(self, additional_served):

        self.number_served += additional_served


restaurant = Restaurant('red robin', 'burgers')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 316
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(5673)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(662)
print(f"Number served: {restaurant.number_served}")

# 9-5: Login attempts


class User():


    def __init__(self, first_name, last_name, username, email, location):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):

        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):

        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):

        self.login_attempts += 1

    def reset_login_attempts(self):

        self.login_attempts = 0

mario = User('mario', 'trujillo', 'mario_t17', 'mario_t17@example.com', 'kansas')
mario.describe_user()
mario.greet_user()

print("\nMaking 3 login attempts...")
mario.increment_login_attempts()
mario.increment_login_attempts()
mario.increment_login_attempts()
print(f"  Login attempts: {mario.login_attempts}")

print("Resetting login attempts...")
mario.reset_login_attempts()
print(f"  Login attempts: {mario.login_attempts}")