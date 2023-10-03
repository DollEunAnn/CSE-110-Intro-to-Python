"""
W02 Team Activity: Areas of Shapes
Dollete, Eunice Ann
"""
import random
magic_num = random.randint(1, 100)

guess_counter = 0
game = True

while game:
    guess_num = int(input('What is your guess? '))

    while guess_num != magic_num:
        if guess_num < magic_num:
            guess_counter = guess_counter + 1
            print('Higher')
            print(f'Guess counter: {guess_counter}')
            guess_num = int(input('What is your guess? '))

        else:
            guess_counter = guess_counter + 1
            print('Lower')
            print(f'Guess counter: {guess_counter}')   
            guess_num = int(input('What is your guess? '))

    print('You guessed it! ')
    print()

    decision = input('Do you want to play again? (yes/no) ')

    if decision.lower() in ['y', 'yes']:
        print()
        guess_counter = 0
        continue
    else:
        print('Bye ~')
        exit()