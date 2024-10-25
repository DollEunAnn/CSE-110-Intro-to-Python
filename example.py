""" 
fruit_count = 0
additional_fruit = int(input('Add some fruit: '))
fruit_basket = 0

fruit_basket = fruit_basket + additional_fruit
print(fruit_basket)



# for the assignment 

game = True
guess_word_count = 0

while game:
    #guess_word_count = guess_word_count + 1
    guess_word_count += 1

    #you code here ....... """

secret = 'mosiah'
guess = ''
guess_word_count = 0

guess = input('Guess:')

while guess != secret:
    print('You guess wrong')
    guess_word_count += 1

    guess = input('Guess:')

    if guess == secret:
        print('Congratulations!')
    
    print(guess_word_count)