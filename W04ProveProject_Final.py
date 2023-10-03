""" 
CSE 110 - Intro to Programming
W04 Prove: Project - Word Puzzle
Dollete, Eunice Ann

"""

game = True

secret_word = 'mosiah'
number_of_secret_word = len(secret_word)


guess_counter = 0
underscore_word = ''

print('Welcome to the word guessing game!')
print()

for letter in secret_word:
     underscore_word += '_ '

print(f'Your hint is: {underscore_word}')

while game:
       print()       
       guess_word = input('What is your guess? ')
       number_of_guess_word = len(guess_word)
       
       guess_counter = guess_counter + 1

       if number_of_secret_word == number_of_guess_word:
             if guess_word.lower() == secret_word:
                print('Congratulations! You guessed it')
                print(f'It took you {guess_counter} guesses.')
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



