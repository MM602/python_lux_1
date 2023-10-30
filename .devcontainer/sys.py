import sys

print("My name is", sys.argv[1])

#Updating the program to eliminate the error
import sys

try:
    print("My name is", sys.argv[1])
except IndexError:
    print("Invalid Argument")

#More Updates
import sys

if len(sys.argv) < 2:
    print("Too few characters")
elif len(sys.argv) > 2:
    print("Too many characters")
else:
    print("My name is", sys.argv[1])

#To ensure it exits after it's successful 
import sys

if len(sys.argv) < 2:
    sys.exit("Too few characters")
elif len(sys.argv) > 2:
    sys.exit("Too many characters")

print("Hello, my name is", sys.argv[1])