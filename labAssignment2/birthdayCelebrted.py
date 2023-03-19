# Taking inputs from user
day_of_birth = int(input("Enter the day of birth: "))
month_of_birth = int(input("Enter the month of birth: "))
year_of_birth = int(input("Enter the year of birth: "))
current_year = int(input("Enter the current year: "))

# Checking for invalid input
if current_year < year_of_birth:
    print("Invalid input")
else:
    # Calculating the number of birthdays celebrated by Mr. X
    if month_of_birth == 2 and day_of_birth == 29:
        # Mr. X was born on 29th Feb
        count = 0
        for year in range(year_of_birth, current_year+1):
            if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
                # Leap year
                count += 1
    else:
        # Mr. X was born on any other day than 29th Feb
        count = current_year - year_of_birth
    
    # Printing the output
    print("Number of birthdays celebrated by Mr. 'X':", count)
