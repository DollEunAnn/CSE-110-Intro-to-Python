
import random

#magic_num = random.randint(1,10)
#magic_num = int(input('What is th magic number? '))
#guess_num = int(input('What is your guess? '))

guess_counter = 0

game = True

while game:
    magic_num = random.randint(1,10)
    guess_num = int(input('What is your guess? '))

    while guess_num != magic_num:
        if guess_num < magic_num:
            guess_counter  += 1
            print('Higher')
            guess_num = int(input('What is your guess? '))
            continue
        else:
            guess_counter  += 1
            print('Lower')    
            guess_num = int(input('What is your guess? '))
            continue

    print('You guessed it! ')
    print(f'Guess counter: {guess_counter}')

    decision = input('Do you want to continue? (yes/no) ')

    if decision.lower() in ['y','yes']:
        print()
        continue
    else:
        break

