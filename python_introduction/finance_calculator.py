#Prompt the user for their monthly income and expenses
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

#Calculate monthly savings
monthly_savings = income - expenses

#Annual savings projection

projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

#output results
print(f"Projected savings after one year, with interest, is: {projected_savings}")
