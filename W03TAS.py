"""
W03 Team Activity: Grade Calculator Program
Dollete, Eunice Ann
"""
# 1 & 2
""" 
grade = float(input('Enter your grade percentage: '))

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
elif grade < 60:
    print('F')

course = False

if grade >= 70:
    passed = input('Did you passed the course? (y/n) ')

    if passed.lower() == 'y':
        print('Congrats! ✨')
    else:
        print('You still nice keep going!') """


# 3

grade = float(input('Enter your grade percentage: '))

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
elif grade < 60:
    letter = 'F'

# get the value of second number
# converts to STR / string first
grade_str = str(grade)
# select the second location count starts at 0, 1
second_digit_grade = int(grade_str[1])

if letter != 'A' and letter != 'F':
    if second_digit_grade >= 7:
        sign = '+'
    else:
        sign = '-'
else:
    sign = ''

print(f'{letter} {sign}')

if grade >= 70:
    passed = input('Did you passed the course? (y/n) ')

    if passed.lower() in ('yes', 'y'):
        print('Congrats! ✨')
    else:
        print('You still nice keep going!')