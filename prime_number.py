# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 305.
# Q 17. Prime Number.

def prime(N):
    if N == 1:
        print("One is neither Prime nor Composite.")
    
    elif N == 0:
        print("Zero is neither Prime nor Composite.")
    
    else:
        flag = 0
        for i in range(2, N):
            if N%i == 0:
                flag = 1
        
        if flag == 1:
            print("N = ", N, "is not a Prime Number.")
        
        else:
            print("N = ", N, "is a Prime Number.")


print("Enter the number...")
N = int(input("N = "))
prime(N)
