# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 569.
# Q. 3 Information Class.


class Information:
    def __init__(self, name, address, age, contact):
        self._name = name
        self._address = address
        self._age = age
        self._contact = contact

    def set_name(self, name):
        self._name = name
    
    def set_address(self, address):
        self._address = address

    def set_age(self, age):
        self._age = age
    
    def set_contact(self, contact):
        self._contact = contact

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_age(self):
        return self._age
    
    def get_contact(self):
        return self._contact
    
def display():
    information_list = []

    for i in range(0, 3):
        if i == 0:
            print("My Information.")
        elif i == 1:
            print("Family Information.")
        else:
            print("Friend Information.")

        name = input("Name: ")
        address = input("Address: ")
        age = input("Age: ")
        contact = input("Contact: ")
        information = Information(name, address, age, contact)
        information_list.append(information)
        print("\n")

    for information in information_list:
        if information is information_list[0]:
            print("My Information.")
        elif information is information_list[1]:
            print("Family Information.")
        else:
            print("Friend Information.")
        print("Name: ", information.get_name())
        print("Address: ", information.get_address())
        print("Age: ", information.get_age())
        print("Contact: ", information.get_contact())

def main():
    display()

main()
