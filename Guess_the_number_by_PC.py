import random

again = True
while again:
    a = 1
    b = 99
    while True :
        hads = random.randint(a, b)
        print(hads, '?')
        x = input('dorost bood : ')
        if(x == 'b'):
            a = hads
        if(x == 'k'):
            b = hads
        if(x == 'd' or a == b):
            print('hahahaha!!!\nThis is Elon Musk.')
            break
    w = input('play Again ?')
    if(w == 'Yes'):
        again = True
    else:
        again = False