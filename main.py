from random import randint, choice
from colorama import Fore, Style

ng = Style.BRIGHT
verd = ng + Fore.GREEN
roxo = ng + Fore.MAGENTA
f = Style.RESET_ALL
cor_pergunta = '\033[37;7m'

cores = ('\033[1;31m', verd, '\033[1;33m', '\033[1;34m', roxo, '\033[1;36m')
dec = 's'
banner = open('banner.txt', 'r').read()

while dec == 's':
    c = 0
    while True:
        print('\x1b[2J\x1b[1;1H')
        n = 0
        ppc = p = ''
        npc = randint(0, 10)
        cor = choice(cores)

        print(banner)
        n = int(input(f'{cor_pergunta}Digite o seu número:{f} '))
        p = input(f'{cor_pergunta}Par ou Ímpar? [P/I]{f} ').strip().upper()[0]
        ppc = 'Ímpar' if 'P' in p else 'Par'
        s = n + npc

        print(f'{roxo}Opções do pc: {f}{ppc}, {npc}')
        if (s % 2 == 0 and p == 'P') or (s % 2 != 0 and p == 'I'):
            print(f'{verd}Você ganhou!!!{f}')
            c += 1
        else:
            print(f'\033[1;31mOps, o computador ganhou de vc...{f}')
            print(f'{roxo}Você ganhou {c} vezes!')
            break
        
        input('\nenter para continuar')

    dec = input(f'{cor_pergunta}Deseja continuar? [s/n] ').strip().lower()[0]
print('\x1b[2J\x1b[1;1H')
print(f'{roxo}Volte sempre ;){f}')
