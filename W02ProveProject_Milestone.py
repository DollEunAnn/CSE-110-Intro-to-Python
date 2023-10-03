""" 
CSE 110 - Intro to Programming
W02 Prove: Project Milestone - Meal Price Calculator
Dollete, Eunice ANn

"""
print()
childMealPrice = float(input("What is the price of a child's meal? "))
adultMealPrice = float(input("What is the price of an adult's meal? "))
childCount = int(input('How many children are there? '))
adultCount = int(input('How many adults are there? '))

childMealPrice_subtotal = childMealPrice * childCount
adultMealPrice_subtotal = adultMealPrice * adultCount

subTotalPrice = childMealPrice_subtotal + adultMealPrice_subtotal

print()
print(f'Subtotal: ${subTotalPrice:.2f}')
print()

saleTaxRate = float(input('What is the sales tax rate? '))

saleTax = subTotalPrice * (saleTaxRate / 100)
totalPrice = subTotalPrice + saleTax

print(f'Sale Tax: ${saleTax:.2f}')
print(f'Total: ${totalPrice:.2f}')
print()

paymentAmount = float(input('What is the payment amount? '))

paymentChangeAmount = paymentAmount - totalPrice

print(f'Change: ${paymentChangeAmount:.2f}')
print()
