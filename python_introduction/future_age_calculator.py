#prompt user for their age
try:
    current_age = int(input("How old are you?: "))
except ValueError:
    print("Input a correct integer")

#calculate age in 2050
future_age = 27 + current_age

#show the results
print(f"In 2050, you will be {future_age} years old")
