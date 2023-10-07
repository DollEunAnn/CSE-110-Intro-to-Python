""" try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        print("Invalid age. Please enter a value between 0 and 120.")
    else:
        print("Your age is:", age)
except ValueError:
    print("Invalid input. Please enter a valid integer.") """


secret_word = 'dog'
guess_word = 'ddd'
number_of_secret_word = len(secret_word)
number_of_guess_word = len(guess_word)
guess_counter = 0
underscore_word = ''

for letter in secret_word:
     underscore_word += '_ '
""" 
if number_of_secret_word == number_of_guess_word:
             if guess_word.lower() == secret_word:
                print('Congratulations! You guessed it')
                print(f'It took you {guess_counter} guesses.')
             else: """

secret_word = 'dog'
guess_word = 'ddd'

for index, letter in enumerate(guess_word):
    if letter in secret_word:
            if_exist = 'it exist'
    else:
            if_exist = "doesn't exist"

    if letter == secret_word[index]:
            if_equal = 'YES'
    else:
            if_equal = 'NO'
            
    print(f'{secret_word[index]} , {letter}, {if_equal} -  {if_exist}')
                    
print()
print()

for index, money in enumerate(guess_word):

    if money in secret_word:
            if_exist = 'it exist'
    else: 
            if_exist = "doesn't exist"

"""  if money == secret_word[index]:
            if_equal = 'YES'
    else:
            if_equal = 'NO' """

#print(f'{secret_word[index]} , {letter}, {if_equal} -  {if_exist}')
print(f'{letter}, {if_equal} -  {if_exist}')

#==========================
