# Lists

""" clients = []
new_client = ''

while new_client != 'quit':
    new_client = input('What is the name of a client? ')
    clients.append(new_client)

for client in clients:
    print(client) """

#########################################

""" friends = ['Anna', 'Bibe', 'Carmela']
tips = [12.25, 13.95, 8.50]

running_total = 0

for tip_amount in tips:
    #running_total = running_total + tip_amount
    running_total += tip_amount

print(f'The total is: {running_total:.2f}') """


######## Creating List ########

""" friends = []
new_friend = ''

while new_friend != 'end':
    new_friend = input('What is the name of a client? ')

    if new_friend != 'end':
        friends.append(new_friend)

print('Your friends are: ')
for friend in friends:
    print(friend) """

######## List Indexes ########

""" friends = []
new_friend = ''

number_of_friends = len(friends)

while new_friend != 'end':
    new_friend = input('What is the name of you friend? ')

    if new_friend != 'end':
        friends.append(new_friend)

print('Your friends are: ')

for friend in friends:
    print(f'{friend}')

for i in range(len(friends)):
    print(f'{i} - {friends[i]}') """
#---------------------------------------------

### Shopping List

shopping_cart = []
new_item = ''

print(f'Please enter the items of the shopping list (type: quit to finish):')

while new_item != 'quit':
    new_item = input('Item: ')

    if new_item != 'quit':
        shopping_cart.append(new_item)

print()
print('The shopping list is:')

for items in shopping_cart:
    print(f'{items.title()}')

print()

print('The shopping list with indexes is: ')

for i in range(len(shopping_cart)):
    print(f'{i}. {shopping_cart[i].title()}')

print()

#remove item
remove_item = int(input('Which item would you like to change? '))

#replace the new item inside the index
new_item = input('What is the new item? ')
shopping_cart[remove_item] = new_item

print()

print('The shopping list with indexes is: ')

for i in range(len(shopping_cart)):
    print(f'{i}. {shopping_cart[i]}')

print()