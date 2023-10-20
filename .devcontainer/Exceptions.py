try:
    x = int(input("Enter the value of x:"))
    print(f"x is {x}")
except ValueError:
    print("x is not a number")

#Integrating the loop function in the code
while True:
    try:
        x = int(input("Enter the value of x:"))
    except ValueError:
        print("x is not a number")
    else:
        break

print(f"x is {x}")

#Writing the code while defining a function
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("Enter the value of x:"))
        except ValueError:
            print("x is not a number")
        else:
            return x

main()

#Using the pass variable for the code
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("Enter the value of x:"))
        except ValueError:
            pass

main()