#Guessing Game Level 3

import random
import time

sec_num3 = random.randint(1, 41)
guess_count = 0
lim3 = 3

print('welcome to the final level. You will get 3 tries to guess the correct integer from 1 to 41')

time.sleep(1.1)

while guess_count < lim3:
    guess = int(input('Enter your guess: ').lower())
    guess_count += 1

    if guess == sec_num3:

        print('You win! You are a master of guessing. Congratulations!')

        time.sleep(3)

        break

else:
    print(f'You lost. Correct answer was {sec_num3}.')

    time.sleep(2)

    quit()
    
    
        
