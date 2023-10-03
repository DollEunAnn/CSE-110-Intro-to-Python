""" 
CSE 110 - Intro to Programming
Week 01 - Prove Project
Dollete, Eunice Ann
"""

# I created a loop where if the user wants to keep creating new story will just loop through the code starting from the beginning. I also put an array of choices for yes and no, so that if the user enter the full word yes/no or only the letter y/n it will be recognize.
# I also combined the adjective and animal input with an article decided by the program to form a title for the story.

vowels = 'aeiou'
article = ''

while True:
    print()
    print('Please enter the following:')
    print()
    adjective = input('adjective: ')
    animal = input('animal: ')
    verb_one = input('verb: ')
    exclamation = input('exclamation: ')
    verb_two = input('verb: ')
    verb_three = input('verb: ')

    if adjective[0].lower() in vowels:
        article = 'an'
    else:
        article = 'a'

    print()

    print('Your story is:')
    print()
    print(f'{article.title()} {adjective.title()} {animal.title()}')
    print()
    print(f"""The other day, I was really in trouble. It all started when I saw a very \n{adjective} {animal} {verb_one} down the hallway. "{exclamation.capitalize()}!" I yelled. But all \nI could think to do was to {verb_two} over and over. Miraculously, \nthat caused it to stop, but not before it tried to {verb_three} \nright in front of my family.""")

    print()

    yes_choices = ['yes', 'y']
    no_choices = ['no', 'n']

    feedback = input('Do you want to create again? (yes/no): ')

    #if yes/y , it will go back to the start of the code.
    #if no/n, it will print 'Okay, bye~' then break/exit the code
    if feedback in yes_choices:
        continue

    print('Okay, bye~ \n')

    #this will break/exit the code
    break