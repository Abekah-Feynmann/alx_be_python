#define global factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#define conversion functions
def convert_to_celsius(fahrenheit):
    return  (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    

def convert_to_fahrenheit(celsius):
    return 32 + (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius)

def main():
    #prompt user for input for a temperature
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").upper()

    #logically convert temperature to the desired units.
    if unit == "F":
        celsius_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {celsius_temp}°C")
    
    elif unit == "C":
        fahrenheit_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {fahrenheit_temp}°F")
    
    else:
        print(f"Invalid temperature.Please enter a numeric value")

if __name__ == "__main__":
    main()



