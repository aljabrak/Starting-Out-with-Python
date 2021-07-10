# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 304.
# Q 13. Prime Number.

g = 9.80665

def falling_distance(x0, t, vi):
    D = x0 + vi*t + (1/2)*g*t**2
    print("Distance Fallen: D = ", format(D, '.5f'))

for x in range(1,10):
    x0 = float(input("Initial Position: x0 = "))
    t = float(input("Free fall time: t = "))
    vi = float(input("Initial Velocity: vi = "))
    falling_distance(x0, t,  vi)
