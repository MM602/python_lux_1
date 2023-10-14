name = input("Enter your name")

if name == "Haaland":
    print("Etihad")
if name == "Jack":
    print("Etihad")
if name == "Anthony":
    print("Trafford")
if name == "Kelvin":
    print("Etihad")
else:
    print("Name not identified")

#Using the or function
name = input("Enter your name")

if name == "Haaland" or name == "Jack":
    print("Etihad")
if name == "Anthony":
    print("Trafford")
if name == "Kelvin":
    print("Etihad")
else:
    print("Name not identified")