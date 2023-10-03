"""
Week 01 Prepare: Learning Activities
Dollete, Eunice Ann
"""

# My First Program
""" color = input('Please type your favorite color:')
print('Your favorite color is')
print(color)

print() """

# Input and Output
# Adjust the Capitalization

#1
""" first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print()
print('Your name is' + ' ' + last_name + ',' + first_name + ' ' + last_name) """


#2 Capitalize
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print()
#print('Your name is' + ' ' + last_name.title() + ', ' + first_name.title() + ' ' + last_name.title())
output = f'Your name is {last_name.title()}, {first_name.title()} {last_name.title()}'
print(output)