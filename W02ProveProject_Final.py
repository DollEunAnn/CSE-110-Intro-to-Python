""" 
CSE 110 - Intro to Programming
W02 Prove: Project Final - Meal Price Calculator
Dollete, Eunice Ann
"""

# I added 'Choose a payment option' where it will ask what kind of payment method they want to pay either 'Cash' or 'Debit/Credit Card'.
# Cash will prompt the 'payment amount' but the Card option will automatically charge the total due amount.
# For the card payment, a summary of card details is displayed but CVV has been modified for into a masked version of the example sensitive data.

print()
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
child_count = int(input('How many children are there? '))
adult_count = int(input('How many adults are there? '))

child_meal_price_subtotal = child_meal_price * child_count
adult_meal_price_subtotal = adult_meal_price * adult_count

sub_total_price = child_meal_price_subtotal + adult_meal_price_subtotal

print()
print(f'Subtotal: ${sub_total_price:.2f}')
print()

sale_tax_rate = float(input('What is the sales tax rate? '))

sale_tax = sub_total_price * (sale_tax_rate / 100)
total_price = sub_total_price + sale_tax

print(f'Sale Tax: ${sale_tax:.2f}')
print(f'Total: ${total_price:.2f}')
print()
    
print('Choose a payment option:')
print('1 : Cash')
print('2 : Debit / Credit Card')

payment_method = int(input('Enter your choice (1/2): '))

def cash_payment_method():
    print()
    payment_amount = float(input('What is the payment amount? '))
    payment_change_amount = payment_amount - total_price
    print(f'Change: ${payment_change_amount:.2f}')
    print()

def card_payment_method():
    print()
    print('Enter the following card details: ')
    card_name = input("Cardholder's name: ")
    card_number = input('Card Number: ')
    card_valid_date = input('Valid Through (MM/DD/YYYY): ')
    card_cvv = input('CVV: ')
    card_cvv_masked = card_cvv[:1] + '****' + card_cvv[3:]
    print(f"""
---------------------------------------------------
Card Holder's Name: {card_name.title()}
Card Number: {card_number}
Card Validity: {card_valid_date}
CVV: {card_cvv_masked}
---------------------------------------------------""")
    print()
    print(f'Your card has been successfully charged with ${total_price:.2f}')
    print(f'Change: $0')
    print()

if payment_method == 1:
    cash_payment_method()
elif payment_method == 2:
    card_payment_method()
else:
    print("Invalid option")
