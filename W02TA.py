"""
W02 Team Activity: Areas of Shapes
Dollete, Eunice Ann
"""
import math

# Area of Square
squareLenght = float(input('What is the lenght of a side of the square? '))
squareArea = squareLenght ** 2
print(f'The area of the square is: {squareArea}')
print(f'The area of the square is: {squareArea / 10000}')

# Area of Rectangle
rectangleLength = float(input('What is the lenght of rectangle? '))
rectangleWidth = float(input('What is the width of rectangle? '))
rectangleArea = rectangleLength * rectangleWidth
print(f'The area of the rectangle is: {rectangleArea}')
print(f'The area of the rectangle is: {rectangleArea / 10000}')


# Area of Circle
circleRadius = float(input('What is the radius of the circle? '))
#circleArea = 3.14 * (circleRadius**2)
circleArea = math.pi * (circleRadius**2)
print(f'The area of the circle is: {circleArea}')
print(f'The area of the rectangle is: {circleArea / 10000}')


