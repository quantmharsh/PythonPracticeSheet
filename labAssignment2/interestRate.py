# Taking inputs from user
initial_amount = float(input("Enter the initial amount: "))
no_of_years = int(input("Enter the number of years of investment: "))
expected_amount = float(input("Enter the expected amount after {} years: ".format(no_of_years)))

# Calculating the rate of interest
rate_of_interest = ((expected_amount - initial_amount) / (initial_amount * no_of_years)) * 100

# Printing the output
print("Rate of interest:", rate_of_interest)
