""" tip = float(input('what is the tip amount? '))

while tip < 0:
    print('Negative tip. Not allowed.')
    tip = float(input('what is the tip amount? '))

print(f'You tip is ${tip:.2f}') """

#------------------------------- While

#Activity 1

""" num = float(input('Please type a positive number: '))

while num < 0:
    print('Sorry, that is a negative number. Please try again.')
    num = float(input('Please type a positive number: '))

print(f'The number is: {num:.0f}') """

# Activity 2
""" decision = input('May I have a piece of candy? ')

while decision.lower() == 'no':
    decision = input('May I have a piece of candy? ' )

print('Thank you.') """

#--------------------------- Loops
# while - trying to find a thing
# for loop - there's a range/ list
""" for index in range(0,2):
    print(index)

names = ['Christoper', 'Susan']
index = 0

while index < len(names):
    print(names[index])
    index = index + 1

numbers = range(100)
for numbers in range(100, 201):
    print(numbers) """


# Activity

""" colors = ["red", "blue", "green", "yellow"]

# 1 for every color in color
for color in colors:
    print(color)

# 2 for loop 1-8
for number in range(1, 9):
    print(number)

# 3 for loop 2-20 even / by two
for numb in range(2, 21, 2):
    print(numb) """


# Looping through Strings
print("This is line one.", end="")
print("This is line two.")