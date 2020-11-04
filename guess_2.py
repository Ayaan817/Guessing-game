#Guessing Game Level 2

import random
import time


print('Welcome to the Guessing Game Level 2')

time.sleep(1.1)                                                       #Makes the program wait for (n) seconds

sec_num2_even = random.randrange(0, 41, 2)                            #This'll generate a random even integer from 1 to 20

sec_num2_odd = random.randrange(0, 40, 1)                             #This'll generate a random odd integer from 1 to 20

lim2 = 5                                                              #This is the max number of tries the user can make

guess_count2 = 0

e_o = str(input("""This game supports 2 modes even and odd. If you enter e or o, you will have to guess even numbers between 0 and 41 or odd numbers between 0 and 41: """).lower())
          

if e_o == 'e': 
    while guess_count2 < lim2:

        guess2 = int(input('Guess even integer from 1 to 40, you have ' + str(lim2 - guess_count2) + ' tries left: '))
        guess_count2 += 1

        if guess2 == sec_num2_even:
            print('You win!')
            response = str(input('To continue to level 3, enter c, to quit, enter q: ').lower())

            if response == 'c':
                from guess_levels import guess_3

            elif response == 'q':

                break

            else:
                print("I don't understand that. Valid inputs are c and q. For disobeying the conditions, you lost.")
                time.sleep(2)
                
                break

    else:
        print(f'You lost! Correct answer was {sec_num2_even}.')

        time.sleep(2)
        quit()

elif e_o == 'o':

    while guess_count2 < lim2:

        guess2 = int(input('Guess odd integer from 1 to 40, you have ' + str(lim2 - guess_count2) + ' tries left: '))
        guess_count2 += 1

        if guess2 == sec_num2_odd:
            print('You win!')
            response = str(input('To continue to level 3, enter c, to quit, enter q: ').lower())

            if response == 'c':
                from guess_levels import guess_3

            elif response == 'q':

                break

            else:
                print("I don't understand that. Valid inputs are c and q. For disobeying the conditions, you lost.")
                time.sleep(2)

                break

    else:
        print(f'You lost! Correct answer was {sec_num2_odd}.')
        time.sleep(2)
        quit()

else:
    print("I don't understand that. Valid inputs are e and o. For disobeying the conditions, you lost.")
    time.sleep(1.1)



    quit()
