""" 
CSE 110 - Intro to Programming
W03 Prove: Project Milestone - Adventure Game
Dollete, Eunice Ann

"""

print()
print('This is a text-based adventure game.')
print("Are you ready? Let's go!")
print("==========================================")
print()
# A cat on the road
print('As you were on your way home from work, you saw a cat on the side of the road.')
check_cross = input('Do you want to CROSS the road to avoid the cat or CHECK on the cat? ')

if check_cross.lower() == 'cross':
    print()
    print('You decided to cross the road. When you looked on you left a large truck is coming your way.')
    flash_survive = input('Do you want to SURVIVE or FLASH your life before your eyes? ')
    print()

    if flash_survive.lower() == 'flash':
        print('Your life flash right before your eyes but before the truck hits you teleport to a different dimension.\nSuddenly, you are facing a cat man. He shows you not one, not two, but three different pills.')
        pill = input('You only need to choose one. BLUE pill or RED pill or WHITE pill? ')
        print()

        if pill.lower() == 'red':
            print('You picked the red pill. After swallowing it, you suddenly transformed into a cat and teleported back to the road you once before but as a cat.')
            print('- END -')
        elif pill.lower() == 'blue':
            print('You picked the blue pill. After swallowing it, you lost conciuseness and by the time you wake up it was time to go home from your work.')
            print('- END -')
        else:
            print("You picked the white pill. After swallowing it, the cat man extend his hand to you. 'Future's gonna be okay.' he said as he shakes yours.\nYou wake up alone in bed remembering the words of the cat man made you smile.")
            print('- END -')
    else:
        print("Miraculously, you we're able to dodge the truck. You heard a series of meow.")
        keep_look = input('Do you want to KEEP walking or LOOK back? ')
        print()

        if keep_look.lower() == 'keep':
            print("You didn't look back. Still shock from the almost accident.")
            print("You're having a weird night, you thought. Since then every time you pass by that road you keep hearing a meow cat even there's nothing.")
            print(" - END - ")
        else:
            print('When you looked back to see the cat is at the middle of the road. As if its the one that pushed you and save you from the truck.')
            print("Can cats really save you? You ask yourself. You feel bad for the cat but there's nothing you can do.")
            print('- END -')
else:
    print()
    print('You decided to check on the cat. Its left front paw is bleeding.')
    help_food = input('Do you want to HELP the cat or just give FOOD from your take-out? ')
    print()

    if help_food.lower() == 'help':
        print()
        print('You helped the cat.')
        home_vet = input('Do you want to bring it HOME or to the VET? ')
        print()

        if home_vet.lower() == 'home':
            print('You have a new pet cat! Yahooo ~ 🐈')
            print('- END -')
        else:
            print('You decided to bring it to the vet nearby. You saved another cat! The vet really appreciates you.')
            print('- END -')
    else:
        print('You reached at your lunchbox. You have leftovers. It starts eating.')
        wait_leave = input('Do you WAIT for the cat to finish or LEAVE? ')
        print()

        if wait_leave.lower() == 'wait':
            print('A large trucked passed by, if you leave that moment you might got hit by it.')
            print('- END -')
        elif wait_leave.lower() == 'leave':
            print('You decided to leave the cat while its eating and continue to walk home.')
            print('- END -')
        else:
            print('Invalid choice. Please choose a valid option.')