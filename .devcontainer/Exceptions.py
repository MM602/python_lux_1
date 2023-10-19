try:
    x = int(input("Enter the value of x:"))
    print(f"x is {x}")
except ValueError:
    print("x is not a number")