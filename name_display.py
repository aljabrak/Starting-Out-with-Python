# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 456.
# Q. 1 Name Display.

name = str(input("Enter Name: "))
name = name.split(" ")
first_name = name[0]
last_name = name[1]
address_name = str(first_name[0].upper() + '.' + last_name[0].upper() + '.')
username = str(first_name[0].lower() + last_name.lower())
print("Name in Address Book: ", address_name)
print("Username: ", username)
