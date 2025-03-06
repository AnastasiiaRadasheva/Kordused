#Kontrolltöö "Kordused"
#V4
#1
#Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n зверьков.
try:
    n = int(input('Sisesta kui palju kordi (1-9): '))

    if n > 1 or n < 9:
        tigr = ''' ^---^  
( o o )  
 ! = !/)  
'''
        print(tigr * n)
    else:
        print('Seda ei saa teha! Sisestage number vahemikus 1 kuni 9.')
except ValueError:
    print('Sisestage palun kehtiv täisarv!')
# 1 ül(второй вариант)
n=int(input("Sisestage number vahemikus 1 kuni 9:"))
for i in range(n):
    print(" ^---^  ",end="  ")
print( )
for i in range(n):
    print("( o o )",end="   ")
print( )
for i in range(n):
    print("! = !/)",end="   ")
#ül 2
#Вывести степени натуральных чисел, не превосходящие данного числа n*100. Пользователь задает показатель степени и число n.
kraad = int(input('kraad'))
n = int(input('sise num'))
maxnum = n * 100
for i in range(1, maxnum+1):
    tulemus = i ** kraad
    if tulemus>maxnum:
        break
    else:
        print(f"{n}^{kraad} = {tulemus}")
#ül 3
#Вывести степени натуральных чисел, не превосходящие данного числа n*100. Пользователь задает показатель степени и число n.
import random

opilased = random.randint(5, 30)  
minhinn = 100  
maxhinn = 1  

for i in range(opilased):
    hinne = random.randint(1, 100)
    minhinn = min(minhinn, hinne)
    maxhinn = max(maxhinn, hinne)

print(f"Kõik õpilased: {opilased}")
print(f"Minimaalne hinne: {minhinn}")
print(f"Maksimaalne hinne: {maxhinn}")
#ül 4
#Одноклеточная амеба каждые 3 часа делится на 2 клетки. Определить, сколько клеток будет через 3, 6, 9, ..., 24 часа, если первоначально была одна амеба.
ameba = 1
for i in range(3, 25, 3):
    ameba *= 2
    print(f"{i} tunni pärast: {ameba} rakku")
#ül 5
#Губка Боб жарит котлеты. Всего у него К котлет, на одну сковородку помещается М котлет.

Расчитать сколько сковородок "полных" надо пожарить и сколько котлет останется еще дожарить на последней. Оформите решение через цикл, используя только вычитание.
try:
    K = int(input("Mitu kotletti: "))
    M = int(input("Mitu kotletti ühel pannil: "))

    if K <= 0 or M <= 0:
        print("Viga! Sisesta positiivne arv.")
    else:
        polnye_skovorodki = K // M  
        ostatok = K % M  

        print(f"On vaja {polnye_skovorodki} täis pannitäit.")
        if ostatok > 0:
            print(f"Viimasel pannil jääb praadida {ostatok} kotletti.")
except ValueError:
    print("Viga! Sisesta täisarv.")
