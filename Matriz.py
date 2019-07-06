import os
from random import randint

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    matriz = []
    limpar()
    print('|-------------|')
    print('| Gerador de  |')
    print('|   Matrizes  |')
    print('|-------------|\n')

    esc = int(input('Deseja escolher o tipo de matriz\nOu deseja definir os valores?\n\n[01]Escolher   [02]Aleatório\n\nR. '))

    if esc == 1:
        limpar()
        linhas = int(input('Digite o número de linhas: '))
        coluna = int(input('Digite o número de colunas: '))
    
    else:
        linhas = randint(1, 9)
        coluna = randint(1, 9)

    limpar()

    print(f'Matriz {linhas}x{coluna}\n')
    for l in range(linhas):
        matriz.append([])
    for m in matriz:
        for c in range(coluna):
            m.append(randint(0, 9))
        print(m)
        
    input()