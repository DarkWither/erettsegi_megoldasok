# Ladányi Attila

# 1.

beker_lottoszamok = input("1. feladat Kérem adja meg az 52. hét lottószámait: ").split() # egyszerre kérjük be az öt számot

lottoszamok_szamkent = [] # számmá alakítjuk a bekért hetet

for szam in beker_lottoszamok:
    lottoszamok_szamkent.append(int(szam))

# 2.

rendezett = sorted(lottoszamok_szamkent)
vissza_stringbe = [str(szam) for szam in rendezett] # kiírás végett

print(f"2. feladat A bekért számok emelkedő sorrendben: {' '.join(vissza_stringbe)}")

# 3.

beker_szam = int(input("3. feladat Kérem adjon meg egy számot 1-51 között: "))

# 4.

lista = [] # két dimenziós lista lesz
fajl = open("lottosz.dat", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip().split()
    lista.append(sor)

print(f"4. feladat A(z) {beker_szam}. hét lottószámai: {' '.join(lista[beker_szam - 1])}") # -1 az index miatt, mivel az 0-tól kezdődik

# 5.

kihuzott_szamok = set() # kigyűjtük a kihúzott számokat, ha pontosan 90 darab, akkor mindegyiket kihúzták, ha nem, akkor volt olyan, amit nem húztak ki

for het in lista:
    for szam in het:
        kihuzott_szamok.add(szam)

print("5. feladat Van-e olyan szám, amit nem húztak ki:")

if len(kihuzott_szamok) == 90:
    print("Nincs")
else:
    print("Van")

# 6.

hanyszor_volt_paratlan = 0

for het in lista:
    volt = False

    for szam in het:
        if int(szam) % 2 == 1:
            volt = True

    if volt:
        hanyszor_volt_paratlan += 1

print(f"6. feladat Összesen {hanyszor_volt_paratlan} héten volt páratlan szám a kihúzottak között.")

# 7.

lista.append(vissza_stringbe)

kiir = open("lotto52.ki", "w", encoding="utf-8")

for het in lista:
    kiir.write(f"{' '.join(het)}\n")

# 8.

szamokat_hanyszor = {}

for szam in range(1, 91):
    szamokat_hanyszor[szam] = 0 # feltöltjük kezdőértékekkel, így ha nem húzták volna ki a számot, akkor 0 lesz a helyén

for het in lista:
    for szam in het:
        szamokat_hanyszor[int(szam)] = szamokat_hanyszor.get(int(szam), 0) + 1

# kiírás

soronkent = 1 # ha 15-tel osztható, akkor sortörés

print("8. feladat A lottószámok gyakorisága:")

for szam in range(1, 91): # azért kell a range, mivel növekvő sorrendbe kell haladni
    if soronkent % 15 == 0:
        print(szamokat_hanyszor[szam])
    else:
        print(szamokat_hanyszor[szam], end=" ")

    soronkent += 1

# 9.

primszamok = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89] # amit kihúztak, azt kiszedjük a listából

for het in lista:
    for szam in het:
        if int(szam) in primszamok:
            primszamok.remove(int(szam))

primszamok_szovegge = []

for szam in primszamok:
    primszamok_szovegge.append(str(szam))

print(f"9. feladat Ezeket a prímszámokat nem húzták ki egyszer sem: {' '.join(primszamok_szovegge)}")
