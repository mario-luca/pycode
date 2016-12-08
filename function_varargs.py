# Learning Python and vim is fun!

def func(a=5, *b, **c):
    print('a', a)

    for single in b:
        print(single)

    for x,y in c.items():
        print(x,y)



func(10, 1, 2, 3, 4, 5,'alpha', 1, 'beta', 2, 'gamma', 3)
