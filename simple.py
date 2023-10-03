""" try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        print("Invalid age. Please enter a value between 0 and 120.")
    else:
        print("Your age is:", age)
except ValueError:
    print("Invalid input. Please enter a valid integer.") """


secret_word = 'mosiah'
guess_word = 'moroni'
number_of_secret_word = len(secret_word)
number_of_guess_word = len(guess_word)
guess_counter = 0
underscore_word = ''

for letter in secret_word:
     underscore_word += '_ '

if number_of_secret_word == number_of_guess_word:
             if guess_word.lower() == secret_word:
                print('Congratulations! You guessed it')
                print(f'It took you {guess_counter} guesses.')
             else:
                for index, letter in enumerate(guess_word): #get the index with the letters
                    if letter in secret_word:
                         in_place = 'it exist'
                    else:
                         in_place = "doesn't exist"

                    if letter == secret_word[index]:
                         equal = 'YES'
                    else:
                         equal = 'NO'
                          
                    print(f'{secret_word[index]} - {letter}, {index}, {equal} -  {in_place} ,  , ')
                    

                    """  if letter in secret_word and letter == secret_word[index]: #check if the letter(from guess) is in secret and have same index
                        if index >= 0:
                            print(f'{letter.upper()} ', end='')       
                     elif letter in secret_word:
                         print(f'{letter} ', end='')
                     else:
                        print('_ ', end='') """