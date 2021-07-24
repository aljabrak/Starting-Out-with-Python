# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 456.
# Q. 2 Sum of Digits in a String.


numbers = str(input('Enter Numbers: '))
sum = 0
for n in range(len(numbers)):
    sum += int(numbers[n])
print('Sum = ', sum)
