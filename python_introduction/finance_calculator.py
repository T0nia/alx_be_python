# Get user input for income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projected annual savings with 5% interest
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Print the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
