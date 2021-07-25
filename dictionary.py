# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 507.
# Q. 5 Galilean Moons of Jupiter.

jupiter_moons = {
    'Io': [{'Mean Radius = ': '1821.6 Km', 'Surface Gravity = ': '1.796 m/sec. squared.', 'Orbital Period = ': '1.769 days'}],
    'Europa': [{'Mean Radius = ': '1560.8 Km', 'Surface Gravity = ': '1.314 m/sec. squared.', 'Orbital Period = ': '3.551 days'}],
    'Ganymede': [{'Mean Radius = ': '2634.1 Km', 'Surface Gravity = ': '1.428 m/sec. squared.', 'Orbital Period = ': '7.154 days'}],
    'Callisto': [{'Mean Radius = ': '2410.3 Km', 'Surface Gravity = ': '1.235 m/sec. squared.', 'Orbital Period = ': '16.689 days'}]
    }

moon_name = str(input("Enter name of Jupiter's Moon: "))

for group in jupiter_moons[moon_name]:
    for key, value in group.items():
        print(key, value)
