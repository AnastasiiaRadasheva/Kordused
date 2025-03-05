#Kontrolltöö "Kordused"
#V4 1 ül
n = int(input('sisesta kui palju kordi(1-9) : '))
try:
    if n<1:
        print('Seda ei saa teha! Sisestage number vahemikus 1 kuni 9')
    elif n>9:
        print('Seda ei saa teha! Sisestage number vahemikus 1 kuni 9')
except:
    print('bebe')
tigr = ''' ^---^
( o o )
 ! = !/)
 
 '''

for i in range(n):
    print(f'{tigr}     ')

#ül 2
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
import random
õpilane = random.randint(5, 30)
minhinn = 101
maxhinn = 0 
for i in range(õpilane):
    grade = random.randint(1, 100)
    if grade < minhinn:
        minhinn = grade 
    if grade > maxhinn:
        maxhinn = grade 
print("kõik õpilane", õpilane)
print("min hinned", minhinn)
print("max hinned", maxhinn)
ül 4
ameba = 1
for i in range(3, 27, 3):
    ameba*=2
    print(ameba)
print(f'rakkude koguarv pärast amööbe {ameba}')

#ül 5
try:
    K = int(input("mitu kotletti: "))
    M = int(input("mitu kotletti ühe panni kohta: "))

    if M < 0:
        print("viga")
    else:
        skokmesta = (K + M - 1) // M 
        print(f"on vaja {skokmesta} praepanni")
        ostanetsja =K%M
        kotleti = m - ostanetsja
        print(f"pannile jäävad kotletid : {kotleti}")
except:
    print("viga ")
