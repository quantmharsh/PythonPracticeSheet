# Taking inputs from user
T = int(input("Enter the total number of nuts and bolts in the bag: "))
N = int(input("Enter the number of nuts in the bag: "))
x = int(input("Enter the percentage of defective nuts in the bag: "))
y = int(input("Enter the percentage of defective bolts in the bag: "))

# Calculating the number of bolts
B = T - N

# Calculating the percentage of non-defective items in the bag
non_defective_percentage = ((100 - x) * N + (100 - y) * B) / T

# Rounding off the answer to two decimal places using format function
print("Percentage of non-defective items in the bag: {:.2f}".format(non_defective_percentage))
