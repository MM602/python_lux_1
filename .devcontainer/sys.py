import sys

print("My name is", sys.argv[1])

#Updating the program to eliminate the error
import sys

try:
    print("My name is", sys.argv[1])
except IndexError:
    print("Invalid Argument")