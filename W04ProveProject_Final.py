""" 
CSE 110 - Intro to Programming
W04 Prove: Project - Word Puzzle
Dollete, Eunice Ann

"""

game = True

secret_word = 'mosiah'
number_of_secret_word = len(secret_word)

guess_counter = 0

print('Welcome to the word guessing game!')
print()
print('Your hint is: _ _ _ _ _ _ ')

while game:       
       guess_word = input('What is your guess? ')
       number_of_guess_word = len(guess_word)
       
       guess_counter = guess_counter + 1

       if number_of_secret_word == number_of_guess_word:
             if guess_word.lower() == secret_word:
                print('Congratulations! You guessed it')
                print(f'It took you {guess_counter} guess(es).')
             else:
                #function send it to loop
                print('Sorry wrong word.')
       else:
           print('Sorry, the guess must have the same number of letters as the secret word.')
           print()



