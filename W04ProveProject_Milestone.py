""" 
CSE 110 - Intro to Programming
W04 Prove: Project Milestone - Word Puzzle
Dollete, Eunice Ann

"""

secret_word = 'mosiah'
guess_counter = 0

print('Welcome to the word guessing game!')

print()

print('Your hint is: _ _ _ _ _ _ ')
guess_word = input('What is your guess? ')

#while guess word is not equal to secret word keep looping
while guess_word.lower() != secret_word:
        guess_counter = guess_counter + 1
        print('Your guess was not correct.')
        guess_word = input('What is your guess? ')

guess_counter = guess_counter + 1
print('Congratulations! You guessed it!')
print(f'It took you {guess_counter} guesses.')


