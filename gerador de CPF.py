import os
from random import *

def limpar():
    sistema = os.name
    if sistema == 'nt':
        os.system("cls")
    else:
        os.system("clear")

n1 = randint(1,9)
n2 = randint(1,9)
n3 = randint(1,9)
n4 = randint(1,9)
n5 = randint(1,9)
n6 = randint(1,9)
n7 = randint(1,9)
n8 = randint(1,9)
n9 = randint(1,9)

calc1 = int((n1 * 10) + (n2 * 9) + (n3 * 8) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (n9 * 2))
div = int(calc1 / 11)
res = calc1 % 11

if res < 2:
    digi1 = 0

else:
    digi1 = 11 - res

calc2 = int((n1 * 11) + (n2 * 10) + (n3 * 9) + (n4 * 8) + (n5 * 7) + (n6 * 6) + (n7 * 5) + (n8 * 4) + (n9 * 3) + (digi1 * 2))
div2 = int(calc2 / 11)
res2 = calc2 % 11

if res2 < 2:
    digi2 = 0

else:
    digi2 = 11 - res2

cpf = (str(n1) + str(n2) + str(n3) + "." + str(n4) + str(n5) + str(n6) + "." + str(n7) + str(n8) + str(n9) + "-" + str(digi1)  + str(digi2))

limpar()
print("Seu CPF é:",cpf)