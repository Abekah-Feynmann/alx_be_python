#import the datetime module
import datetime

current_date = datetime.datetime.now()

#create the display_current_datetime function
def display_current_datetime():
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_current_date)

#calculate future date function
def calculate_future_date(n):
    future_date = current_date + datetime.timedelta(days=n)
    return future_date 
    

def main():
    #display the current date and time
    display_current_datetime()

    #prompt the user to enter a number of days
    numb_days = int(input("Enter the number of days to add to the current date: "))

    #calculate the future date
    future_date = calculate_future_date(numb_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


if __name__ == "__main__":
    main()