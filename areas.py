import math

side = float(input("Enter side of the square: "))
square_area = side * side
print(f"Area of Square: {square_area}")

base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
triangle_area = 0.5 * base * height  
print(f"Area of Triangle: {triangle_area}")

length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
rectangle_area = length * width  
print(f"Area of Rectangle: {rectangle_area}")

radius = float(input("Enter radius of the circle: "))
circle_area = math.pi * radius*radius  
print(f"Area of Circle: {circle_area}")
