"""
W02 Team Activity: Areas of Shapes
Strech Challenge

Dollete, Eunice Ann

"""
# Single lenght value

import math 

lengthCentimeter = float(input('Enter the length in centimeters: '))

squareArea = lengthCentimeter ** 2
circleArea = math.pi * (lengthCentimeter ** 2)
cubeVolume = lengthCentimeter ** 3
sphereVolume = (4 / 3) * math.pi * (lengthCentimeter ** 3)

print(f'Area of square: {squareArea}')
print(f'Area of circle {circleArea}')
print(f'Volume of cube {cubeVolume}')
print(f'Volume of sphere {sphereVolume}')

#if converted use 10000 
# if 100, then convert
############################################################

#convert to square centimeters 
squareArea_sq_cm = squareArea / 10000
circleArea_sq_cm = circleArea / 10000
cubeVolume_sq_cm = cubeVolume / 10000
sphereVolume_sq_cm = sphereVolume / 10000

print()
print(f'Area of square: {squareArea_sq_cm} square meters ')
print(f'Area of circle {circleArea_sq_cm} square meters')
print(f'Volume of cube {cubeVolume} square meters')
print(f'Volume of sphere {cubeVolume_sq_cm} square meters')

