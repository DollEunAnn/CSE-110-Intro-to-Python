"""
W02 Team Activity: Areas of Shapes
Dollete, Eunice Ann
"""

import random

number = random.randint(1, 10)

#magic_num = int(input('What is th magic number? '))
magic_num = random.randint(1, 100)
guess_num = int(input('What is your guess? '))

if guess_num != magic_num:
    if guess_num < magic_num:
        print('Higher')
    else:
        print('Lower')    
else:
    print('You guessed it! ')

#======================================

while guess_num != magic_num:
    if guess_num < magic_num:
        print('Higher')
        guess_num = int(input('What is your guess? '))
        continue
    else:
        print('Lower')    
        guess_num = int(input('What is your guess? '))
        continue

print('You guessed it! ')