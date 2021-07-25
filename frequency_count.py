# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 508.
# Q. 5 Random Number Frequencies.


from numpy import *

frequency = {}
number = random.randint(1, 11, 100)
number.sort()
print(number)

for element in number:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

for key, value in frequency.items():
    print(key, ": ", value)
