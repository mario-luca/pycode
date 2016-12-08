# Learning vim is fun!

while True:
    s = raw_input('Enter a string: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small.')
        continue

    print('Input is of sufficent length!')

