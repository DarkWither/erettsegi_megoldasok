# Ladányi Attila

# 1.

class Szallitasok:
    def __init__(self, mikor_tettek_szalagra, honnan, hova, tomeg):
        self.mikor_tettek_szalagra = int(mikor_tettek_szalagra)
        self.honnan = int(honnan)
        self.hova = int(hova)
        self.tomeg = int(tomeg)

    def __repr__(self):
        return f"{self.mikor_tettek_szalagra} {self.honnan} {self.hova} {self.tomeg}"


lista = []

fajl = open("szallit.txt", "r", encoding="utf-8")

elso_sor = fajl.readline().strip().split() # így néz ki: ["200", "3"]
szalag_hossza = int(elso_sor[0])
egysegnyi_elmozdulashoz_ido = int(elso_sor[1]) # mennyi idő alatt mozdul meg a szalag egy egységet

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Szallitasok(*sor))

# 2.

beker_szallitas_sorszam = int(input("2. feladat\nAdja meg, melyik adatsorra kíváncsi! "))

beker_szallitas = lista[beker_szallitas_sorszam - 1] # -1 azért, mert a lista első eleme 0., a szállításoknál meg 1.

print(f"Honnan: {beker_szallitas.honnan} Hova: {beker_szallitas.hova}")

# 3.

def tav(szalaghossz, indulashelye, erkezeshelye):
    # két lehetőség

    if indulashelye < erkezeshelye: # ha nem megy körbe a szalagon, akkor
        return erkezeshelye - indulashelye
    elif erkezeshelye < indulashelye: # ha körbemegy a szalagon
        return szalaghossz - indulashelye + erkezeshelye # (szalaghossz - indulashelye) = a végéig a táv, (+ erkezeshelye) majd az elejétől az érkezés helyéig a táv

# 4.

legnagyobb_tavolsag = 0

for szallitas in lista: # megkeressük a legnagyobb távolságot
    if legnagyobb_tavolsag < tav(szalag_hossza, szallitas.honnan, szallitas.hova):
        legnagyobb_tavolsag = tav(szalag_hossza, szallitas.honnan, szallitas.hova)

print(f"\n4. feladat\nA legnagyobb távolság: {legnagyobb_tavolsag}")

maximalis_tavolsagu_szallitasok = [] # azoknak a szállításoknak a sorszámai, melyek hossza a legnagyobb távolság

for sorszam in range(1, len(lista) + 1): # kiindulás az egy, mivel az első szállítás sorszáma 1.; utolsó len(lista) + 1, így csak len(lista) lesz még benne, ami az utolsó szállítás sorszáma
    vizsgalt_szallitas = lista[sorszam - 1] # a sorszámhoz melyik listaelem tartozik, -1 mert az index 0-tól kezdődik

    if legnagyobb_tavolsag == tav(szalag_hossza, vizsgalt_szallitas.honnan, vizsgalt_szallitas.hova):
        maximalis_tavolsagu_szallitasok.append(str(sorszam)) # ha a szállítás távolsága a legnagyobb, akkor a sorszámát hozzáadjuk a listához, str() a .join() miatt

print(f"A maximális távolságú szállítások sorszáma: {' '.join(maximalis_tavolsagu_szallitasok)}")

# 5.

# Azok a szállítmányok haladnak el, amelyek körbemennek a szalagon, azaz az érkezés kisebb, mint az indulás

ossztomeg = 0

for szallitas in lista:
    if szallitas.honnan > szallitas.hova:
        ossztomeg += szallitas.tomeg

print(f"\n5. feladat\nA kezdőpont előtt elhaladó rekeszek össztömege: {ossztomeg}")

# 6.

beker_idopont = int(input("\n6. feladat\nAdja meg a kívánt időpontot! "))
szallitott_rekeszek = [] # melyik rekeszek voltak akkor a szalagon

for sorszam in range(1, len(lista) + 1):
    vizsgalt_szallitas = lista[sorszam - 1] # lásd 4. feladat

    # mikor ér célba = mikor_került_fel + tav * egysegnyi_elmozdulashoz_ido

    mikor_er_celba = vizsgalt_szallitas.mikor_tettek_szalagra + tav(szalag_hossza, vizsgalt_szallitas.honnan, vizsgalt_szallitas.hova) * egysegnyi_elmozdulashoz_ido

    # az időpontnak nagyobbnak, vagy egyenlőnek kell lennie az indulási időponttal és (szigorúan) kisebbnek a célbaérésnél

    if vizsgalt_szallitas.mikor_tettek_szalagra <= beker_idopont and mikor_er_celba > beker_idopont:
        szallitott_rekeszek.append(str(sorszam)) # str() a .join() miatt

print(f"A szállított rekeszek halmaza: {' '.join(szallitott_rekeszek)}")

# 7.

kiir = open("tomeg.txt", "w", encoding="utf-8")

helyekrol_ossztomeg = {} # kulcs: hely, érték: össztömeg, amely rekeszeket ott raktak fel

for szallitas in lista:
    helyekrol_ossztomeg[szallitas.honnan] = helyekrol_ossztomeg.get(szallitas.honnan, 0) + szallitas.tomeg

for hely in sorted(helyekrol_ossztomeg.keys()): # a rendezett kulcsokon megyünk végig, hogy sorrendbe legyenek a helyek (nem muszáj, simán is végig lehet menni a szótáron és úgy kiírni, de így hasonlít legjobban a mintára)
    kiir.write(f"{hely} {helyekrol_ossztomeg[hely]}\n") # helyekrol_ossztomeg[hely] = a helyekrol_ossztomeg szótárban a hely kulcshoz tartozó érték
