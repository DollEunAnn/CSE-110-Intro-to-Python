"""
Week 03 Prepare: Learning Activities
Dollete, Eunice Ann

"""
""" from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.now())


first_name = 'Eunice'
print_time('printed first name')

for x in range(0,10):
    print(x)
print_time('completed loop') """


""" # return
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
first_name_inital = get_initial(first_name, False)

#print('Your initial is:' + first_name_inital)
print(get_initial(first_name)) """

# Activity
""" def display_regular(value):
    return value
    
def display_uppercase(value):
    uppercase_value = value.upper()
    return uppercase_value

def display_lowercase(value):
    lowercase_value = value.lower()
    return lowercase_value

message = input('What is your message? ')
print(display_regular(message))
print(display_uppercase(message))
print(display_lowercase(message)) """

# ==========function part 2 activity============= #

import math 

def compute_area_square(length):
    square_area = length ** 2
    return square_area

def compute_area_rectangle(width, length):
    rectangle_area = width * length
    return rectangle_area

def compute_area_circle(radius):
    circle_area = math.pi * (radius ** 2)
    return circle_area

while True:
    print()
    print('Pick an option:')
    print('1. Square')
    print('2. Rectangle')
    print('3. Circle')
    print("Type 'QUIT' to end the program.")

    choice = input('What kind of shape? (square, rectangle, circle):  ')

    if choice.lower() == 'square':
        #square
        square_length = float(input('What is the length of a side of the square? '))
        #square_area = compute_area_square(square_length)
        square_area = compute_area_rectangle(width=square_length, length=square_length)

        print(f'The area of the square is: {square_area}')

    elif choice.lower() == 'rectangle':
        #rectangle
        rectangle_length = float(input('What is the length of rectangle? '))
        rectangle_width = float(input('What is the width of rectangle? '))
        rectangle_area = compute_area_rectangle(rectangle_width, rectangle_length)

        print(f'The area of the rectangle is: {rectangle_area}')
    
    elif choice.lower() == 'circle':
        #circle
        circle_radius = float(input('What is radius of the circle? '))
        circle_area = compute_area_circle(circle_radius)

        print(f'The area of the circle is: {round(circle_area,2)}')

    elif choice.lower() == 'quit':
        break
    else:
        print()
        print('Please enter a valid option.')
        continue















