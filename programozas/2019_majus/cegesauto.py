# Ladányi Attila

# 1.

class Autok:
    def __init__(self, nap, idopont, rendszam, szemely_azonosito, km_ora, ki_be_hajtas):
        self.nap = int(nap)
        self.idopont = idopont
        self.rendszam = rendszam
        self.szemely_azonosito = int(szemely_azonosito)
        self.km_ora = int(km_ora)
        self.ki_be_hajtas = int(ki_be_hajtas)

    def __repr__(self):
        return f"{self.nap} {self.idopont} {self.rendszam} {self.szemely_azonosito} {self.km_ora} {self.ki_be_hajtas}"


lista = []

fajl = open("autok.txt", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Autok(*sor))

# 2.

elvittek_lista = []

for auto in lista:
    if auto.ki_be_hajtas == 0:
        elvittek_lista.append(auto)

print(f"2. feladat\n{elvittek_lista[-1].nap}. nap rendszám: {elvittek_lista[-1].rendszam}")

# 3.

beker_nap = int(input("3. feladat\nNap: "))

print(f"Forgalom a(z) {beker_nap}. napon:")

for auto in lista:
    if auto.nap == beker_nap:
        if auto.ki_be_hajtas == 0:
            print(f"{auto.idopont} {auto.rendszam} {auto.szemely_azonosito} ki")
        elif auto.ki_be_hajtas == 1:
            print(f"{auto.idopont} {auto.rendszam} {auto.szemely_azonosito} be")

# 4.

# Az az autó nem volt bent a hónap végén, amelyik utolsó ki_be_hajtas-a 0

utolso_ki_be_hajtasok = {} # kulcs: rendszám, érték: utolsó ki_be_hajtas száma

for auto in lista:
    utolso_ki_be_hajtasok[auto.rendszam] = auto.ki_be_hajtas

# Meg kell számolni, hogy az előbb létrehozott szótár kulcsai között hány 0 van

mennyit_nem_hoztak_vissza = 0

for ki_be in utolso_ki_be_hajtasok.values():
    if ki_be == 0:
        mennyit_nem_hoztak_vissza += 1

print(f"4. feladat\nA hónap végén {mennyit_nem_hoztak_vissza} autót nem hoztak vissza.")

# 5.

autok_rendszamai = [] # az autók rendszámai

for szam in range(300, 310):
    autok_rendszamai.append(f"CEG{szam}")

print("5. feladat")

for rendszam in autok_rendszamai:
    # megtett_távolság = utolsó_kilóméteróra_állás - első_kilóméteróra_állás

    rendszamhoz_tartozo_hajtasok = []

    for auto in lista:
        if auto.rendszam == rendszam:
            rendszamhoz_tartozo_hajtasok.append(auto)

    print(f"{rendszam} {rendszamhoz_tartozo_hajtasok[-1].km_ora - rendszamhoz_tartozo_hajtasok[0].km_ora} km")

# 6.

utak = [] # kétdimenziós lista lesz, egy elem: [kihajtás, behajtás]

for auto in lista:
    if auto.ki_be_hajtas == 0: # csak kihajtásnál keresünk behajtást
        volt_mar = False # volt-e már kihajtás: ha nem, csak akkor adunk hozzá utat; azért, hogy ha ugyanazt az autót ugyanaz a személy kétszer hozná vissza, mert kétszer vitte el, akkor az külön legyen

        for hajtas in lista: # végigmegyünk mégegyszer a listán, hogy megkeressük a behajtást
            if auto.szemely_azonosito == hajtas.szemely_azonosito and auto.rendszam == hajtas.rendszam and hajtas.ki_be_hajtas == 1: # azonosítók, rendszámok egyezzenek, és behajtás legyen
                if not volt_mar:
                    utak.append([auto, hajtas])
                    volt_mar = True

leghosszabb_ut_tav = 0 # leghosszabb távolság
leghosszabb_ut_szemely = 0 # aki megtette ezt az utat

for ut in utak:
    tav = ut[1].km_ora - ut[0].km_ora

    if tav > leghosszabb_ut_tav:
        leghosszabb_ut_tav = tav
        leghosszabb_ut_szemely = ut[0].szemely_azonosito

print(f"6. feladat\nLeghosszabb út: {leghosszabb_ut_tav} km, személy: {leghosszabb_ut_szemely}")

# 7.

beker_rendszam = input("7. feladat\nRendszám: ")

kiir = open(f"{beker_rendszam}_menetlevel.txt", "w", encoding="utf-8")

for auto in lista:
    if auto.rendszam == beker_rendszam:
        if auto.ki_be_hajtas == 0: # kihajtás esetén:
            kiir.write(f"{auto.szemely_azonosito}\t{auto.nap}.\t{auto.idopont}\t{auto.km_ora} km")
        elif auto.ki_be_hajtas == 1: # behajtás esetén:
            kiir.write(f"\t{auto.nap}.\t{auto.idopont}\t{auto.km_ora} km\n")

print("Menetlevél kész.")
