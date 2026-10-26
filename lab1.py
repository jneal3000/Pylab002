import math

# Problem 1
area = math.pi * 5**2
print("Area of the circle is",area)


volume = (4 / 3) * math.pi * 3**3
print("Volume of the sphere",volume)


hypotenuse = math.sqrt(3**2 + 4**2)
print("Hypotenuse of the sphere",hypotenuse)

# Problem 2

name = "Joshua Neal"
first_name = "Joshua"
last_name = "Neal"
full_name = first_name + " " + last_name
print(full_name)

print(full_name.upper())
print(full_name.lower())

# Problem 3

age = 20
height = 6.5
weight = 189

print(type(age))
print(type(height))
print(type(weight))

height_inches = 6 * 12 + 6
bmi = (189 / height_inches**2) * 703

print("BMI: ",bmi)
