import time
import random

eric = 200
john = 200
dragon = 300


print('''
    welcome Lord,
    You can spin the wheel of fate
    See how your Knights fare
    Against the dragon:
    press "enter" ''')

while eric >= 0 or john >= 0 and dragon >= 0:
    go = input('>>')
    if go == 'exit':
        break
    if go == '':
        hit = random.randint(5, 20)
        who = random.randint(0,2)
        if who == 0:
            eric -= hit
            print(f'eric was hit {hit}, new health {eric}')
        elif who == 1:
            john -= hit
            print(f'john was hit {hit}, new health {john}')
        else:
            dragon -= hit
            print(f'dragon was hit {hit}, new health {dragon}')
        print(f'''
            eric health: {eric}
            john health: {john}
            dragon health: {dragon}''')
        print('\n\troll again or "exit" to give up')
if dragon > 0:
    print("dragon wins!\t" * 3)
else:
    print('you win!\t' * 3)

