
import math

name = "Joshua Neal"
age = 20
height = 6.6
favorite_color = "red"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"My name is {name}")
print(f"My age is {age}")
print(f"My height is {height}")
print(f"My favorite color is {favorite_color}")

print("Age: {:d}".format(age))
print("Height: {:.2f}".format(height))
print(f"Age squared: {age:d}")

print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite color: {favorite_color}
""")

print(f"""
      Name: {name}
      Age: {age}
      Height: {height}
      Favorite color: {favorite_color}
""")

radius = 5
circle_area = math.pi * radius ** 2
print(f"Circle area: {circle_area:.1f}")

print("Square root of age:", math.sqrt(age))

print("Sine of height:", math.sin(height))
print("Cosine of height:", math.cos(height))

print("Age plus 5:", age + 5)
print("Height minus 4:", height - 4)
print("Age times height:", age * height)
print("Height divided by 2:", height / 2)
print("Age divided by 3, remainder:", age % 3)
print("Age squared:", age ** 2)
print("Integer division of height by 2:", height // 2)

fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit} F is equal to {celsius:.1f} C")

