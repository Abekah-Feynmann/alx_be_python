#prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

#generate the pattern
i = 0
while i < size:
    for j in range(size):
        print("*", end = "")
    print()
    i += 1
    