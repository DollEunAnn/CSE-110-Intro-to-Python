"""
Week 03 Prepare: Learning Activities
Dollete, Eunice Ann
"""

####################LA 1
""" price = 0
if price >= 1.00:
    tax = .07
else:
    tax = 0

country = input("What country do you live in? ")

if country.lower() == 'canada':
    province = input("What province do you live in? ")
    tax = 0
    if province.capitalize() in('Alberta', 'Nunavit', 'Yukon'):
        tax = 0.05
    elif province.capitalize() == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0

print(tax) """


""" first_number = input('What is the first number? ')
second_number = input('What is the second number? ')


if first_number > second_number:
    print('The first number is greater')
else:
    print('The first number is not greater')


if first_number == second_number:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if first_number < second_number:
    print('The second number is greater')
else:
    print('The second number is not greater')

print()

fav_animal = 'cat'
animal = input('What is your favorite animal? ')

if animal.lower() == fav_animal:
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.') """

###################LA 2
# Requirements for honour roll
# Minimum 85% grade point average
# Lowest greate is atleast 70%

#highest_grade = float(input('Highest grade: '))
""" gpa = float(input('GPA: '))
lowest_grade = float(input('Lowest grade: '))

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print('Well done')
else:
    print('Sorry, maybe next time.') """

""" 
if (x > 5 or x < -5) and y > 10:
# In this case, x can either be greater than 5 or less than negative 5, and y must
# always be greater than 10

if x > 5 or x < -5 and y > 10:
# Without parentheses, the x < -5 and y > 10 conditions go together and both must be
# true, unless x > 5, in which case the whole statement is true 
"""


# The Problem: Qualifying for a Loan
print()
print('Rate from 1 - 10 the following: ')
print()
loan_size = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income_level = int(input('How high is your income? '))
downpayment_level = int(input('How large is your downpayment? '))

# How large the loan --- at least 5
if loan_size >= 5:
    if credit_history >= 7 and income_level >= 7:
        decision = True
    elif downpayment_level >= 5:
        decision = True
    else:
        decision = False       
else:
    #check if credit is less than 4 
    if credit_history >= 4:
        if income_level >= 7 or downpayment_level >= 7:
            decision = True
        elif income_level >= 4 and downpayment_level >= 4 :
            decision = True   
        else:
            decision = False
    else:
        decision = False
        

if decision:
    print('YES')
else:
    print('NO')

#For Testing
# 8, 7, 8, 1 - YES ✅
# 5 2 7 5 - YES ✅
# 8 2 8 3 - NO ✅
# 2 4 1 7 - YES ✅
# 4 5 5 3 - NO ✅