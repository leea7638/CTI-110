"""
(block comments -- continue until the triple quotes end)
# CTI 110
# P2LAB1
# Austin Lee
# 9/15/2026
Get Radius, calculate and display radius, circumference, and area
"""
PI = 3.14159 # Constant - do not change
# Input -- get radius
radius = float(input("what is the radius of the circle? "))

# Calculation -- find diameter, circumference, and area
# diameter = 2*r, circumference = 2*pi*r, area = pi*r*r
diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius

# Output -- .1f, .2f, .3f
print(f"the diameter is {diameter:.1f}")
print(f"the circumference is {circumference:.2f}")
print(f"the area is {area:.3f}")