#prompt a user to input a task description
task = input("Enter your task:").capitalize()

#prompt the user to input the task's priority
priority = input("Priority (high/medium/low): ").lower()

#prompt the user to indicate if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = f"{task} is a {priority} priority task"

#match task priority using a matchcase statement
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Reminder: {reminder}. Consider completing it when there is free time")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {reminder}. However, it needs to be completed today!")
        else:
            print(f"Reminder: {reminder}. Consider completing it on your spare time")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {reminder}. Work on {task} during the final working hour of the day")
        else:
            print(f"Reminder: {reminder}. Consider completing it when you have free time")
    case _:
        print("Choose the appropriate responses")

