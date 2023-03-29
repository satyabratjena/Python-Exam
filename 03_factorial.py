l1 = int(input("Enter a non-negative integer:"))

if l1 < 0:
    print("ERROR!!!")
    print(f"{l1}Please enter a valid input")

else:
    fac = 1
    for i in range(1, l1 + 1):
        fac *= i
    print("The factorial of", l1, "is", fac, ".")