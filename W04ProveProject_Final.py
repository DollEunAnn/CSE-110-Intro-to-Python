""" 
CSE 110 - Intro to Programming
W04 Prove: Project - Word Puzzle
Dollete, Eunice Ann

"""

# I added an option where they can choose a category of what word they want to guess. 
# I list down 5 categories then a random function will choose a word inside the array.
# I also included a while loop to keep asking for the right option of category if the user entered an option more than 5 or less than 1
  
import random

game = True
guess_counter = 0
underscore_word = ''
set_list = ''

fruits = ['apple', 'banana', 'watermelon', 'grape', 'mango']
colors = ['red', 'blue', 'green', 'yellow', 'purple']
countries = ['USA', 'Canada', 'France', 'Japan', 'Philippines']
animals = ['cat', 'horse', 'koala', 'fish', 'dog']
programming_languages = ['Python', 'Java', 'JavaScript', 'PHP', 'Ruby']

print()
print('Welcome to the word guessing game!')
print()
print('Choose a category of word:')
print('1. Fruits')
print('2. Colors')
print('3. Countries')
print('4. Animals')
print('5. Programming Languages')

print()
category = int(input('Enter the number of the desired category (1-5): '))

while category > 5 or category < 1:
    print('Invalid option')
    category = int(input('Enter the number of the desired category (1-5): '))

if category == 1:
    set_list = fruits
    set_name = 'fruits'
elif category == 2:
    set_list = colors
    set_name = 'colors'
elif category == 3:
    set_list = countries
    set_name = 'countries'
elif category == 4:
    set_list = animals
    set_name = 'animals'
else:
    set_list = programming_languages
    set_name = 'programming languages'

print()
print(f'You choose: {set_name.title()}')

secret_word = 'dog'
#secret_word = random.choice(set_list)

number_of_secret_word = len(secret_word)

for letter in secret_word:
     underscore_word += '_ '

print(f'Your hint is: {underscore_word}')

while game:
       print()       
       guess_word = input('What is your guess? ')
       number_of_guess_word = len(guess_word)

       #convert the words to lowercase
       guess_word = guess_word.lower()
       secret_word = secret_word.lower()
       
       guess_counter = guess_counter + 1

        #verify guess_word length
       if number_of_secret_word == number_of_guess_word: 
             if guess_word == secret_word:
                print('Congratulations! You guessed it!')
                print(f'It took you {guess_counter} guesses.')
                print()
                break
             else:
                print('Your hint is: ', end='')
                for index, letter in enumerate(guess_word):
                     if letter in secret_word and letter == secret_word[index]:
                         print(f'{letter.upper()} ', end='')       
                     elif letter in secret_word:
                         print(f'{letter} ', end='')
                     else:
                        print('_ ', end='')                
       else:
           print('Sorry, the guess must have the same number of letters as the secret word.')



