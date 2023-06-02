import random

again = True
while again:
    javab = random.randint(1, 99)
    while True:
        try:
            hads = int(input('your hads : '))
        except:
            hads = int(input('your hads : '))
        if(hads > javab):
            print('koochaktar')
        if(hads < javab):
            print('bozorgtar')
        if(hads == javab):
            print('wowowwwowow!!!!\nYou are Eloon Musk')
            break
    b = input('play Again ? ')
    if(b == 'Yes'):
        again = True
    else:
        again = False