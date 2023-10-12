x = int(input("Enter the value of x:"))

if x % 2 == 0:
    print("x is an even number")
else:
    print("x is an odd number")

#Defining a function: is_even
def main():
    z = int(input("Enter the value of z:"))
    if is_even(z):
        print("z is an even number")
    else:
        print("z is an odd number")

def is_even(y):
    if y % 2 == 0:
        return True
    else:
        return False
    
main()