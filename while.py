number = 42
running = True

while running == True:
    guess = int(input('Enter an integer: '))
    if guess == number:
        print('You guessed the number!')
        running = False
    elif guess < number:
        print('You guessed too low!')
    else:
        print('You guessed too high!')
else:
    print('The while loop is over.')

print('Done')
