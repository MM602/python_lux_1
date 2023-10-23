def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for k in range(n):
        print("Q#" * (k + 1))

if __name__ == "__main__":
    main()