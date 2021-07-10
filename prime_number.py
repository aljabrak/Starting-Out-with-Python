# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 305.
# Q 17. Prime Number.

def prime(N):
    flag = 0
    for i in range(2, N):
        if N%i == 0:
            flag = 1
    if flag == 1:
        print("N is not a Prime Number.")
    else:
        print("N is a Prime Number.")


print("Enter the number...")
N = int(input("N = "))
prime(N)
