""" 
CSE 110 - Intro to Programming
W05 Prove: Project Milestone - Shopping Cart
Dollete, Eunice Ann

"""

# Variables
shopping_cart = []
add_item = ''


# Start of Program

print('Welcome to the Shopping Cart Program!\n')

while True:
    print('Please select one of the following:')
    print('1. Add a new item')
    print('2. Display the contents of the shopping cart')
    print('3. Remove an item') 
    print('4. Compute the total') 
    print('5. Quit')

    user_option = int(input('Please enter an action: '))

    # Menu 1 - Add a new item
    if user_option == 1:
        add_item = input('What item would you like to add? ')

        shopping_cart.append(add_item)
        
        #get the latest item
        latest_item = shopping_cart[-1]

        print(f"'{latest_item}' has been added to the cart.")
        print()
        continue

    # Menu 2 - View Cart
    if user_option == 2:
        print('The contents of the shopping cart are:')

        for item in shopping_cart:
            print(item)
        print()

    if user_option == 5:
        print('Thank you. Goodbye.')
        break