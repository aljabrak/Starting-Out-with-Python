# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 305.
# Q 19. Loan Payment.

def loan_payment(R, A, M):
    R_ = 1 + R
    P = (R*A)/(1 - pow(R_, -M))
    print("Monthly Interest Rate = ", R*100, "%")
    print("Monthly Payment: P = ", P)


R = float(input("Enter Monthly Interest Rate: R = "))
A = float(input("Enter Loan Amount: A = "))
M = float(input("Enter Number of Months: M = "))
loan_payment(R, A, M)
