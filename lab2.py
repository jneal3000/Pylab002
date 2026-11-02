
import math

# Part 1: Variables and Assignments

# Create variables
name = "Joshua Neal"
age = 20
height = 6.5
favorite_color = "Red"

# 1. Print one variable at a time
print(name)
print(age)
print(height)
print(favorite_color)

# 2. Print all variables using commas
print(name, age, height, favorite_color)

# 3. Print using f-strings and format specifiers
print(f"My name is {name} and my favorite color is {favorite_color}.")
print(f"Age: {age:d}")
print(f"Height: {height:.2f} feet")

# 4. Print using a multi-line formatted string
print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite Color: {favorite_color}
""")

# Calculate area of a circle
radius = 5
circle_area = math.pi * radius ** 2
print(f"Circle area: {circle_area:.1f}")


# Part 2: Statements and Modules

# Calculate square root of age
square_root = math.sqrt(age)
print("Square root of age:", square_root)

# Calculate sine and cosine of height
sine_height = math.sin(height)
cosine_height = math.cos(height)

print("Sine of height:", sine_height)
print("Cosine of height:", cosine_height)


# Part 3: Expressions and Operators

# Arithmetic calculations
sum_result = age + 5
difference_result = height - 4
product_result = age * height
quotient_result = height / 2
remainder_result = age % 3
power_result = age ** 2

# Print results
print("Age plus 5:", sum_result)
print("Height minus 4:", difference_result)
print("Age times height:", product_result)
print("Height divided by 2:", quotient_result)
print("Age divided by 3 remainder:", remainder_result)
print("Age squared:", power_result)


# Part 4: Temperature Conversion

# Ask user for Fahrenheit temperature
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Print converted temperature
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")


