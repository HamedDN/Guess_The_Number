import random

again = True
while again:
    a = 1
    b = 100
    while True :
        hads = random.randint(a, b)
        print(hads, '?')
        x = input('dorost bood : ')
        if(x == 'b'):
            a = hads +1
        if(x == 'k'):
            b = hads -1
        if(x == 'd' or a == b):
            print('hahahaha!!!\nThis is Eloon Musk.')
            break
    w = input('play Again ?')
    if(w == 'Yes'):
        again = True
    else:
        again = False