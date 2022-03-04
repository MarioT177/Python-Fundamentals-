# 2-3 personal message

name = "Mario"
print(f"Hello {name.title()}, would you like to learn some python today?")

# 2-4 Name cases

name = "Mario"
print(name.title())
print(name.upper())
print(name.lower())


#2-5 Famous quote

name = "Marcus Aurelius"
print(f'{name.title()} once said,"The happiness of your life depends upon the quality of your thoughts." ')

#2-6 Famous quote

famous_person = "Marcus Aurelius"
message = 'once said,"The happiness of your life depends upon the quality of your thoughts."'
print(famous_person.title(), message)
#2-7 stripping names

name = "\t Mario Trujillo \n"
print(name)

print(name.lstrip())

print(name.rstrip())

print(name.strip())


