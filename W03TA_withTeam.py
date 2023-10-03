grade = float(input('What is your grade percentage? '))

""" #1
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

#2
if grade >= 70:
    print('Congrats! You passed!')
else:
    print('You can still try again next time.')
 """

#3
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

print(letter)



#####

#stretch challenge
grade_str = str(grade)

second_digit_grade = int(grade_str[1])

grade_remainder = grade % 10

if grade >= 93:
    sign = ''
elif grade_remainder >= 7:
    sign = '+'
elif grade_remainder < 3: 
    sign = '-'
else:
    sign = ''



print(f'{letter} {sign}')



