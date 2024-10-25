list_names = [ "Add item", "View cart", "Remove item", "Compute total", "Quit"] 
numbers = [1,2,3,4,5] 
choice = ''
new_entry = ''

print("Welcome to the Shopping Cart Program!")
print()


#Here the user has different option to choose
print("Please select one of the following:")
for i, j in zip (numbers, list_names):
    print(i, j)

 
#Here I'm trying to retrieve input data from user and treat them.
while new_entry != quit:
    new_entry = int(input("Please enter an action:"))
    if new_entry == numbers[0]:
        choice = input("What item would you like to add?:") 
        price = input(f'What is the price of {choice}?')
        print (f'{choice} has been added to the cart.') 
    elif new_entry == numbers[1]:
        print("The contents of the shopping cart are:") 
        print(f'{choice} ${price}')
    elif new_entry == numbers[2]:
        item =int(input("which item would you like to remove?"))
    elif new_entry == numbers[3]:
        print(f"The total price of the items in the shopping cart is ${price}")
    else:
        break

    