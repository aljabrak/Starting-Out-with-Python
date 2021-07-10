# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 225.
# 5. A loop which calculates the series sum of 1/30 + 2/29 + 3/28 + ... + 30/1

num = 1             # Numerator of First Term.
den = 30            # Denominator of First Term.
sum = 0.0

for x in range(31):
    num = x
    den = 30-x+1
    sum += num/den
print("Sum = ", format(sum, '.36f'))
