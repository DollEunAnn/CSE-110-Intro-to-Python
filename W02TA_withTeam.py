"""
W02 Team Activity: Areas of Shapes
Dollete, Eunice Ann

with Team
"""
import math 

#divide it to 10,000 after conversion

#square
square_length = float(input('What is the length of a side of the square? '))

square_area = square_length ** 2
squareArea_sq_cm = square_area / 10000

print(f'The area of the square is: {square_area}')
print(f'Area of square: {squareArea_sq_cm} square meters ')

#rectangle
rectangle_length = float(input('What is the length of rectangle? '))
rectangle_width = float(input('What is the width of rectangle? '))

rectangle_area = rectangle_width * rectangle_length
rectangle_sq_cm = rectangle_area / 10000

print(f'The area of the rectangle is: {rectangle_area}')
print(f'Area of square: {rectangle_sq_cm} square meters ')

#circle
circle_radius = float(input('What is radius of the circle? '))

circle_area = math.pi * (circle_radius ** 2)
circleArea_sq_cm = circle_area / 10000

print(f'The area of the circle is: {round(circle_area,2)}')
print(f'Area of circle {round(circleArea_sq_cm,2)} square meters')






""" length = float(input('Enter the length: '))

squareArea = length ** 2
circleArea = math.pi * (length ** 2)
cubeVolume = length ** 3
sphereVolume = (4 / 3) * math.pi * (length ** 3)

print(f'Area of square: {squareArea}')
print(f'Area of circle {circleArea}')
print(f'Volume of cube {cubeVolume}')
print(f'Volume of sphere {sphereVolume}') """





