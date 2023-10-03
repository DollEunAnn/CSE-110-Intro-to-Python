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

print(f'Your hint is {underscore_word}')

while game:
       print()       
       guess_word = input('What is your guess? ')
       number_of_guess_word = len(guess_word)
       
       guess_counter = guess_counter + 1

       if number_of_secret_word == number_of_guess_word:
             if guess_word.lower() == secret_word:
                print('Congratulations! You guessed it')
                print(f'It took you {guess_counter} guess(es).')
                break
             else:
                #check if the letter exist in the word
                for letter in guess_word:
                     if letter in secret_word:
                        print(letter, end='')
                     else:
                        print('_ ', end='')

                print()
                print()

                for index, letter in enumerate(guess_word):
                     if letter in secret_word or letter == secret_word[index]:
                        if index >= 0:
                            print(f'{letter.upper()} ', end='')
                     else:
                        print('_ ', end='')

                print()
                print()

                for index, letter in enumerate(guess_word):
                     if letter in secret_word and letter == secret_word[index]:
                        if index >= 0:
                            print(f'{letter.upper()} ', end='')       
                     elif letter in secret_word:
                         print(f'{letter} ', end='')
                     else:
                        print('_ ', end='')

                #print('Sorry wrong word.')
       else:
           print('Sorry, the guess must have the same number of letters as the secret word.')
           print()



