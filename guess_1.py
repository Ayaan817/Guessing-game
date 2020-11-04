#Guessing Game Level 1

import random
import time

print('Welcome to the Guessing Game')

time.sleep(1.1)                                                       #Makes the program wait for (n) seconds

sec_num1 = random.randint(1, 10)                                      #This'll generate a random integer from 1 to 10

lim1 = 5                                                              #This is the max number of tries the user can make

guess_count1 = 0

while guess_count1 < lim1:

    guess1 = int(input('Guess integer from 1 to 10, you have ' + str(lim1 - guess_count1) + ' tries left: '))
    guess_count1 += 1

    if guess1 == sec_num1:
        print('You win!')
        response = str(input('To continue to level 2, enter c, to quit, enter q: ').lower())

        if response == 'c':

            #Guessing Game Level 2

            from guess_levels import guess_2

        elif response == 'q':

            break

        else:
            print("I don't understand that. Valid inputs are c and q. For disobeying the conditions, you lost.")

            break

else:
    print(f'You lost! Correct answer was {sec_num1}')
    time.sleep(1.1)

    play = str(input("Play again?(enter 'yes' or 'no') ").lower())

    while play != 'no':
        if play == 'yes':
            from guess_levels import guess_1
        else:
            print("I don't understand that.")
            quit()

        
