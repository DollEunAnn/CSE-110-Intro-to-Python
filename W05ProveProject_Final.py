""" 
CSE 110 - Intro to Programming
W05 Prove: Project Milestone - Shopping Cart
Dollete, Eunice Ann

"""
# I created a function view_cart to display the contents of the cart and also tells if its empty.
# If the cart is empty for Menu 2, 3, and 5 it will show a message.
# I reuse my code from W02 Meal Price Calucator for the Menu 5 I added which is the payment method.

# Variables
shopping_cart = []
shopping_cart_prices = []
total_price = 0.0
add_item = ''
add_price = 0.0
remove_item = ''

# Function
# view all cart items
def view_cart():
    if shopping_cart:
        for i in range(len(shopping_cart)):
                print(f'{i+1}. {shopping_cart[i].title()} - ${shopping_cart_prices[i]:.2f}')
    else:
        print('The cart is empty.')
    
# payment method
def cash_payment_method(total_price):
    print()
    payment_amount = float(input('What is the payment amount? '))
    payment_change_amount = payment_amount - total_price
    print(f'Change: ${payment_change_amount:.2f}')
    print()
    shopping_cart.clear()
    shopping_cart_prices.clear()

def card_payment_method(total_price):
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
    shopping_cart.clear()
    shopping_cart_prices.clear()

# Start of Program
print()
print('===============================================')
print()
print('Welcome to the Shopping Cart Program!\n')

while True:
    print('===============================================')  
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View Cart')
    print('3. Remove an item') 
    print('4. Compute total')
    print('5. Checkout and Pay') 
    print('6. Quit')

    print()
    user_option = int(input('Please enter an action: '))   

    # Menu 1 - Add item
    if user_option == 1:
        print()
        add_item = input('What item would you like to add? ')
        add_price = float(input(f"What is the price of '{add_item.title()}'? "))

        shopping_cart.append(add_item)
        shopping_cart_prices.append(add_price)
        
        #get the latest item
        latest_item = shopping_cart[-1]

        print(f"'{latest_item.title()}' has been added to the cart.")
        print()

    # Menu 2 - View Cart
    if user_option == 2:
        print()
        print('The contents of the shopping cart are:')
        print()
        view_cart()       
        print()

    # Menu 3 - Remove Item
    if user_option == 3:
        print()
        if not shopping_cart:
            print("The cart is empty. There's nothing to remove.")
            print()  
        else:
            print()
            print('Your shopping cart items:')
            view_cart()
            print()

            remove_item = int(input('Which item would you like to remove? '))

            # adjust index to -1 to access it to the list right index
            remove_item -= 1

            if 0 <= remove_item < len(shopping_cart):

                # remove the item in both list
                shopping_cart.pop(remove_item)
                shopping_cart_prices.pop(remove_item)

                print('Item removed.')
                print()
                print('Updated list of your cart:')
                view_cart()
                print()


            else:
                print('That item is not valid.')


    # Menu 4 - Compute total
    if user_option == 4:
        for price in shopping_cart_prices:
            total_price += price
        print()
        print(f'The total price of the items in the shopping cart is ${total_price:.2f}')
        print()

        #return the value to 0 because it keeps the amount computed last time
        total_price = 0  

    # Menu 5 - Checkout and Pay
    if user_option == 5:
        if not shopping_cart:
            print()
            print("The cart is empty. There's nothing to pay.")
            print()
        else:  
            print()
            print('Choose a payment option:')
            print('1 : Cash')
            print('2 : Debit / Credit Card')

            payment_method = int(input('Enter your choice (1/2): '))

            for price in shopping_cart_prices:
                total_price += price

            if payment_method == 1:
                cash_payment_method(total_price)
            elif payment_method == 2:
                card_payment_method(total_price)
            else:
                print("Invalid option")


    # Menu 6 - Exit
    if user_option == 6:
        print('Thank you. Goodbye.')
        break
        
    if user_option not in [1, 2, 3, 4, 5, 6]:
        print()
        print('That option is not available.')
        print()