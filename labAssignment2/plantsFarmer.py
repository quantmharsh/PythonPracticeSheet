# Taking inputs from user
length = int(input("Enter the length of the farm (in feet): "))
breadth = int(input("Enter the breadth of the farm (in feet): "))

# Calculating the number of rows and columns
rows = (length-2) // 4 + 1
columns = (breadth-2) // 4 + 1

# Calculating the total number of plants required
total_plants = rows * columns

# Printing the output
print("Number of rows:", rows)
print("Number of columns:", columns)
print("Number of plants required:", total_plants)
