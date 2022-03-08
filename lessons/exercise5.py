# 1 (5-1)

car = 'Ford'
print("Is car == 'ford'? I predict True.")
print(car == 'Ford')

print("\nIs car == 'Ford'? I predict False.")
print(car == 'ford')


horse = 'Mustang'
print("is horse == 'mustang'? I predict True")
print(horse =='Mustang')

print("\nIs horse == 'Mustang'? I predict False.")
print(horse == 'mustang')


phone = 'Iphone'
print("is phone == 'iphone' I predict True")
print(phone == 'Iphone')

print("\nIs phone == 'iphone' I predict False")
print(phone == 'iphone')


shoe  = 'Nike'
print("is shoe == 'Nike' I predict True")
print(phone == 'Nike')

print("\nIs shoe == 'nike' I predict False")
print(shoe == 'Nike')


drink = 'Coke'
print("is drink == 'Coke' I predict True")
print(drink == 'coke')

print("\nIs drink == 'coke' I predict False")
print(drink == 'Coke')



# 2 (5-2)


car = 'Ford'
print("\nIs car == 'Ford'? I predict False.")
print(car == 'ford')

print("\nIs car == 'Ford'? I predict True.")
print(car.lower() == 'ford')
print('\n')
age = 25
if age == 26:
    print('You can come in!')
else:
    print("You can't come in!")

print('\n')
age = 28
if age >= 23:
    print('You can come in!')
else:
    print("You can't come in!")

print('\n')
age = 26
if age >= 23 and age >=28:
    print('You can come in!')
else:
    print("You can't come in!")

print('\n')
age = 19
if age <= 20 or age >=29:
    print('You can come in!')
else:
    print("You can't come in!")
print('\n')
car = ['ford', 'honda', 'chevy']
print('ford' in car)
print('chevy' in car)
print('nissan' in car)
print('\n')
cars = ['ford', 'honda', 'chevy']
car_name = 'nissan'
if car_name not in cars:
    print("It isn't")
else:
    print("It is")

# 3.

def arithmatic_operators(value1, value2):
    result_add = value1 + value2
    result_subtract = value1 - value2
    result_multi = value1 * value2
    result_divide = value1 / value2
    result_modulus = value1 % value2
    result_exponent = value1 ** value2
    result_floor = value1 // value2
    print(result_add)
    print(result_subtract)
    print(result_multi)
    print(result_divide)
    print(result_modulus)
    print(result_exponent)
    print(result_floor)



arithmatic_operators(20, 5)


# 4

def assign_operators(value1):
    value1 %= 30
    print(value1)
    value1 **= 8
    print(value1)
    value1 -= 50
    print(value1)
    value1 += 25
    print(value1)


assign_operators(50)







