#prompt the user for the weather today
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

#conditions for user responses.
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.") 
elif weather == "rainy":
    print("Don't forget umbrella and coat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
