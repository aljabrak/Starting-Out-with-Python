# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 424.
# Q. 1 Valid Number Information.

numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
numbers.sort()
print('Numbers = ', numbers)
valid_numbers = []

for x in numbers:
    if x >= 0:
        valid_numbers.append(x)

print('Valid Numbers = ', valid_numbers)

total = 0
for x in valid_numbers:
    total += x 
    
print('Total = ', total)
average = total/len(valid_numbers)
print('Average = ', average)
