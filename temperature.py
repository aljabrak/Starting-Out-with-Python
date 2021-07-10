# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 187.
# Chemical Labs Inc.
temperature = float(input("Read Temperature of Substance: "))

while temperature > 102.5:
	print("Turn Down Thermostat.")
	print("Wait for 5 minutes.")
	temperature = float(input("Read Temperature of Substance (After 5 minutes.): "))

print("Temperature is acceptable.")
print("Check again after 15 minutes.")
