# 1 8-15: Printing Models

import printing_functions as pf

car_models = ['ford', 'chevy', 'dodge']
completed_models = []

pf.print_models(car_models, completed_models)
pf.show_completed_models(completed_models)

# 8-16:Imports


import car_functions
this_car = car_functions.make_car('acura','tlx', year=2015, color='white')


print(this_car)


from car_functions import make_car
this_car = make_car('acura', 'tlx', year=2015, color='white')
print(this_car)


from car_functions import make_car as mc
this_car = mc('acura', 'tlx', year=2015, colour='white')
print(this_car)


import car_functions as ic
this_car = ic.make_car('acura', 'tlx', year=2015, color='white')
print(this_car)


from car_functions import *
this_car = make_car('acura', 'tlx', year=2015, color='white')
print(this_car)

# 2 9-10: Imported Restaurant:

from restaurant import Restaurant

Red_Robin = Restaurant('Red Robin', 'gourmet burgers')
Red_Robin.describe_restaurant()
Red_Robin.open_restaurant()

# 9-11: Imported Admin

from user import Admin

mario = Admin('mario', 'trujillo', 'mario_t17', 'mario_t17@example.com', 'kansas')
mario.describe_user()

mario_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts', ]

mario.privileges.privileges = mario_privileges

print(f"\nThe admin {mario.username} has these privileges: ")
mario.privileges.show_privileges()

# 9-12: Multiple Modules


from admin import Admin

mario = Admin('mario', 'trujillo', 'mario_t17', 'mario_t17@example.com', 'kansas')
mario.describe_user()

mario_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
mario.privileges.privileges = mario_privileges

print(f"\nThe admin {mario.username} has these privileges: ")
mario.privileges.show_privileges()


# 3 9-16:







