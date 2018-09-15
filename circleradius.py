import math
def area(radius):
    return math.pi * radius**2

radius = float(input("Radius (in feet)"))
while (radius <= 0):
    radius = float(input("Error!! Radius must be positive. Radius: "))

print ("Area: ", area(radius), "sq ft")