weight_pounds = float(input("Enter weight in pounds: "))
height_inches = float(input("Enter height in inches: "))

# Convert weight from pounds to kilograms
weight_kg = weight_pounds * 0.4536

# Convert height from inches to meters
height_m = height_inches * 0.0254

# Calculate BMI using the formula
bmi = weight_kg / (height_m * height_m)

print("BMI of the person is:", round(bmi, 2))
