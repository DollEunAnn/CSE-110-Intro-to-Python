""" 
CSE 110 - Intro to Programming
W03 Prove: Project Final - Adventure Game
Dollete, Eunice Ann

"""

# I added way where i can count how many times does the user entered an invalid option. If it reaches to 3, the game will automatically ends.
# At the same time, to help me warn the user I made a function - invalid_input_notif()

# My sister played the game and her feedback was, she doesn't know the first time that she need to choose between the capitalize letters
# so I ended up putting an instructions before the start of the game. When my mother played this time, she keeps putting space accidentally so I also
# included a strip() function. They said it was fun and I also happy that they enjoyed it.


invalid_input_count = 0

text_end = '''                                              
                 __                                                
                /\ \                                               
   __    ___    \_\ \                                      
 /'__`\/' _ `\  /'_` \                                  
/\  __//\ \/\ \/\ \L\ \                                 
\ \____\ \_\ \_\ \___,_\                                  
 \/____/\/_/\/_/\/__,_ /                                    

'''

# to display appropriate messages when a user enters an invalid option
def invalid_input_notif():
    if invalid_input_count == 2:
        print()
        print('You already entered an invalid option twice. Please be careful.')
        print()
    elif invalid_input_count == 3:
        print()
        print(text_end)
        print("Your adventure ends here.\nA invalid option cause you a life and you used them all.")
        print()
        exit()
    else:
        print()
    

print()
print("=======================================================")
print('This is a text-based adventure game.')
print('Please choose between the CAPITALIZE letters carefully.')
print("Are you ready? Let's go!")
print("=======================================================")
print()




#CHECK or CROSS
print('As you were on your way home from work, you saw a cat on the side of the road.')

while True:
    invalid_input_notif()
    check_cross = input('Do you want to CROSS the road to avoid the cat or CHECK on the cat? ')

    # CROSS
    if check_cross.strip().lower() == 'cross':
        print('You decided to cross the road. When you looked on you left a large truck is coming your way.')

        while True:
            invalid_input_notif()
            flash_survive = input('Do you want to SURVIVE or FLASH your life before your eyes? ')
            # FLASH
            if flash_survive.strip().lower() == 'flash':
                print('Your life flash right before your eyes but before the truck hits you teleport to a different dimension.\nSuddenly, you are facing a cat man. He shows you not one, not two, but three different pills.')
                while True:
                    invalid_input_notif()
                    pill = input('You only need to choose one. BLUE pill or RED pill or WHITE pill? ')
                    # RED
                    if pill.strip().lower() == 'red':
                        print('You picked the red pill. After swallowing it, you suddenly transformed into a cat and teleported back to the road you once before but as a cat.')
                        print()
                        print(text_end)
                    # BLUE
                    elif pill.strip().lower() == 'blue':
                        print('You picked the blue pill. After swallowing it, you lost conciuseness and by the time you wake up it was time to go home from your work.')
                        print()
                        print(text_end)
                    # WHITE
                    elif pill.strip().lower() == 'white':
                        print("You picked the white pill. After swallowing it, the cat man extend his hand to you. 'Future's gonna be okay.' he said as he shakes yours.\nYou wake up alone in bed remembering the words of the cat man made you smile.")
                        print()
                        print(text_end)
                    # Invalid input
                    else:
                        invalid_input_count += 1
                        print()
                        if invalid_input_count != 3:
                            print('Invalid option. Please choose between RED, BLUE, and WHITE.')
                        continue
                    break

            #SURVIVE
            elif flash_survive.strip().lower() == 'survive':
                print("Miraculously, you we're able to dodge the truck. You heard a series of meow.")

                while True:
                    invalid_input_notif()
                    keep_look = input('Do you want to KEEP walking or LOOK back? ')
                    #KEEP
                    if keep_look.strip().lower() == 'keep':
                        print("You didn't look back. Still shock from the almost accident.")
                        print("You're having a weird night, you thought. Since then every time you pass by that road you keep hearing a meow cat even there's nothing.")
                        print()
                        print(text_end)
                    #LOOK
                    elif keep_look.strip().lower() == 'look':
                        print('When you looked back to see the cat is at the middle of the road. As if its the one that pushed you and save you from the truck.')
                        print("Can cats really save you? You ask yourself. You feel bad for the cat but there's nothing you can do.")
                        print()
                        print(text_end)
                    #Invalid input
                    else:
                        invalid_input_count += 1
                        print()
                        if invalid_input_count != 3:
                            print('Invalid option. Please choose between KEEP and LOOK.')
                        continue
                    break            
            #Invalid input
            else:
                invalid_input_count += 1
                print()
                if invalid_input_count != 3:
                    print('Invalid option. Please choose between SURVIVE and FLASH.')
                continue
            break
        
    # CHECK
    elif check_cross.strip().lower() == 'check':
        print('You decided to check on the cat. Its left front paw is bleeding.')

        while True:
            invalid_input_notif()
            help_food = input('Do you want to HELP the cat or just give FOOD from your take-out? ')
            # HELP
            if help_food.strip().lower() == 'help':
                print('You decided to helped the cat.')
                while True:
                    invalid_input_notif()
                    home_vet = input('Do you want to bring it HOME or to the VET? ')
                    # HOME
                    if home_vet.strip().lower() == 'home':
                        print('You have a new pet cat! Yahooo ~ 🐈')
                        print()
                        print(text_end)
                    # VET
                    elif home_vet.strip().lower() == 'vet':
                        print('You decided to bring it to the vet nearby. You saved another cat! The vet really appreciates you.')
                        print()
                        print(text_end)
                    #Invalid option
                    else:
                        invalid_input_count += 1
                        print()
                        if invalid_input_count != 3:
                            print('Invalid option. Please choose between HOME and VET.')
                        continue
                    break
            # FOOD
            elif help_food.strip().lower() == 'food':
                print('You reached at your lunchbox to give the cat some food.\nYou have leftovers. It starts eating.')
                while True:
                    invalid_input_notif()
                    wait_leave = input('Do you WAIT for the cat to finish or LEAVE? ')
                    if wait_leave.strip().lower() == 'wait':
                        print('A large trucked passed by, if you leave that moment you might got hit by it.')
                        print()
                        print(text_end)
                    elif wait_leave.strip().lower() == 'leave':
                        print('You decided to leave the cat while its eating and continue to walk home.')
                        print()
                        print(text_end)
                    else:
                        invalid_input_count += 1
                        print()
                        if invalid_input_count != 3:
                            print('Invalid option. Please choose between WAIT and LEAVE.')
                        continue
                    break
            else:
                invalid_input_count += 1
                print()
                if invalid_input_count != 3:
                    print('Invalid option. Please choose between HELP and FOOD.')
                continue
            break
    else:
        invalid_input_count += 1
        print()
        if invalid_input_count != 3:
            print('Invalid option. Please choose between CROSS and CHECK.')
        continue
    break

choice = 'YES'


if choice == 'YES':
    [do something here]
elif choise == 'NO':
    [do something here]
else:
    [do something here]