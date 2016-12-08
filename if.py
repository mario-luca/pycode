number = 42
guess = int(input('Please enter an integer: '))

if guess == number:
    print('You guessed the number!')
elif guess < number:
    print('The number is lower than your guess.')
else:
    print('The number is higher than your guess.')

print('Done')

