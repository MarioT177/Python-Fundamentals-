# 1  5-8 Hello Admin:

usernames = ['Bob', 'Tim', 'Rob', 'Dave', 'Steve']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for loggin in again!")



#   5-9 No users:

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for loggin in again!")
else:
    print("We need to find some users!")

# 2   5-10: Checking usernames


current_users = ['james', 'mario', 'jesus', 'antonio', 'Oscar']
new_users = ['paul', 'Mario', 'Freddy', 'angel', 'Ivan']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")




# 3   5-11: Ordinal Numbers


numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")



# 4    6-1: Person


person = {
    'first_name': 'Oscar',
    'last_name': 'Gomez',
    'age': 26,
    'city': 'wichita',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


# 5    6-7: People

people = []


person = {
    'first_name': 'oscar',
    'last_name': 'gomez',
    'age': 26,
    'city': 'wichita',
}
people.append(person)

person = {
    'first_name': 'mario',
    'last_name': 'trujillo',
    'age': 26,
    'city': 'wichita',
}
people.append(person)

person = {
    'first_name': 'maria',
    'last_name': 'trujillo',
    'age': 49,
    'city': 'wichita',
}
people.append(person)


for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")