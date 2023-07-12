# Ladányi Attila

# 1.

class Athaladasok:
    def __init__(self, ora, perc, azonosito, irany):
        self.ora = int(ora)
        self.perc = int(perc)
        self.azonosito = int(azonosito)
        self.irany = irany

    def __repr__(self):
        return f"{self.ora} {self.perc} {self.azonosito} {self.irany}"

    def idopont_percben(self):
        # az áthaladás időpontja percekben
        return (self.ora * 60) + self.perc

lista = []

fajl = open("ajto.txt", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Athaladasok(*sor))

# 2.

belepesek_lista = []

for athaladas in lista:
    if athaladas.irany == "be":
        belepesek_lista.append(athaladas)

kilepesek_lista = []

for athaladas in lista:
    if athaladas.irany == "ki":
        kilepesek_lista.append(athaladas)

print(f"2. feladat\nAz első belépő: {belepesek_lista[0].azonosito}\nAz utolsó kilépő: {kilepesek_lista[-1].azonosito}")

# 3.

ki_hanyszor = {} # kulcs: azonositó, érték: áthaladások száma

for athaladas in lista:
    ki_hanyszor[athaladas.azonosito] = ki_hanyszor.get(athaladas.azonosito, 0) + 1

legnagyobb_azonosito = 0 # azért szükséges, mert eddig fog menni majd a for ciklusunk

for athaladas in lista:
    if athaladas.azonosito > legnagyobb_azonosito:
        legnagyobb_azonosito = athaladas.azonosito

kiir = open("athaladas.txt", "w", encoding="utf-8")

for azonosito in sorted(ki_hanyszor.keys()): # a kulcsok növekvő sorrendjén megyünk végig
    kiir.write(f"{azonosito} {ki_hanyszor[azonosito]}\n")

# 4.

# Megoldás elve: az tartózkodott a végén a társalgóban, akinek a legutolsó áthaladásának iránya "ki"
# Időrenddel szerencsére nem kell foglalkoznunk, ugyanis az áthaladásokat időrendben rögzítették,
# így a legkésőbbi áthaladás egyben az utolsó is

vegen = [] # azonosítók, akik a végén bent voltak

for azonosito in sorted(ki_hanyszor.keys()): # növekvő sorrend miatt
    utolso_athaladas = 0

    for athaladas in lista:
        if athaladas.azonosito == azonosito:
            utolso_athaladas = athaladas # időrend miatt a legutolsó lesz az értéke

    if utolso_athaladas.irany == "be":
        vegen.append(str(azonosito)) # str() a join miatt

print(f"\n4. feladat\nA végén a társalgóban voltak: {' '.join(vegen)}")

# 5.

legtobben_mikor = [0, 0, 0] # [óra, perc, emberek] hány ember tartózkodott abban az időpontban

for ora in range(9, 16): # 9 és 15 között vizsgálták az áthaladásokat
    if ora == 15: # ha 15 az óra, akkor csak a 15:00 időpontot kell vizsgálni, utána lévőket nem
        abban_az_idopontban = 0 # abban az időpontban hány ember tartózkodott a társalgóban

        for athaladas in lista:
            if athaladas.idopont_percben() <= (15 * 60): # ha abban az időpontban van áthaladás, akkor még azt is beleszámoljuk
                if athaladas.irany == "be":
                    abban_az_idopontban += 1
                elif athaladas.irany == "ki":
                    abban_az_idopontban -= 1

        if abban_az_idopontban > legtobben_mikor[2]:
            legtobben_mikor = [15, 0, abban_az_idopontban]

    else:
        for perc in range(0, 60):
            percekben = (ora * 60) + perc # az időpont percekben

            abban_az_idopontban = 0

            for athaladas in lista:
                if athaladas.idopont_percben() <= percekben:
                    if athaladas.irany == "be":
                        abban_az_idopontban += 1
                    elif athaladas.irany == "ki":
                        abban_az_idopontban -= 1

            if abban_az_idopontban > legtobben_mikor[2]:
                legtobben_mikor = [ora, perc, abban_az_idopontban]

print(f"\n5. feladat\nPéldául {legtobben_mikor[0]}:{legtobben_mikor[1]}-kor voltak a legtöbben a társalgóban.")

# 6.

beker_azonosito = int(input("\n6. feladat\nAdja meg a személy azonosítóját! "))

# 7. és 8.

# A két feladatot egyszerre oldjuk meg

beker_azonosito_athaladasok = [] # a bekért azonosító áthaladásai

for athaladas in lista:
    if athaladas.azonosito == beker_azonosito:
        beker_azonosito_athaladasok.append(athaladas)

if len(beker_azonosito_athaladasok) % 2 == 0: # ha páros számú áthaladás van, az azt jelenti, hogy a végén nem volt bent a társalgóban
    athaladasok_ideje = "" # a mintán szereplő időpontok
    elozo_athaladas = 0 # a for ciklusban a ciklusváltozó előtti áthaladás
    bent_toltott_ido = 0

    for athaladas in beker_azonosito_athaladasok:
        if athaladas.irany == "be": # a "-"-jel bal oldalán lesz
            athaladasok_ideje += f"{athaladas.ora}:{athaladas.perc}-"
        elif athaladas.irany == "ki": # ha kimegy, akkor a "-" jel jobb oldalán
            athaladasok_ideje += f"{athaladas.ora}:{athaladas.perc}\n" # sortörés, hogy alatta legyen a következő

            bent_toltott_ido += (athaladas.idopont_percben() - elozo_athaladas.idopont_percben())

        elozo_athaladas = athaladas

    # 7. feladat kiírása

    print(f"\n7. feladat\n{athaladasok_ideje}")

    # 8. feladat kiírása

    print(f"8. feladat\nA(z) {beker_azonosito}. személy összesen {bent_toltott_ido} percet volt bent, a megfigyelés végén nem volt a társalgóban.")
else:
    athaladasok_ideje = ""  # a mintán szereplő időpontok
    elozo_athaladas = 0  # a for ciklusban a ciklusváltozó előtti áthaladás
    bent_toltott_ido = 0

    for athaladas in beker_azonosito_athaladasok:
        if athaladas.irany == "be":  # a "-"-jel bal oldalán lesz
            athaladasok_ideje += f"{athaladas.ora}:{athaladas.perc}-"

            if athaladas == beker_azonosito_athaladasok[-1]: # ha az utolsó áthaladást vizsgáljuk, akkor a bent töltött időt úgy számoljuk, hogy 15 órából kivonjuk a belépés idejét
                bent_toltott_ido += ((15 * 60) - athaladas.idopont_percben())

        elif athaladas.irany == "ki":  # ha kimegy, akkor a "-" jel jobb oldalán
            athaladasok_ideje += f"{athaladas.ora}:{athaladas.perc}\n"  # sortörés, hogy alatta legyen a következő

            bent_toltott_ido += (athaladas.idopont_percben() - elozo_athaladas.idopont_percben())

        elozo_athaladas = athaladas

    # 7. feladat kiírása

    print(f"\n7. feladat\n{athaladasok_ideje}")

    # 8. feladat kiírása

    print(f"\n8. feladat\nA(z) {beker_azonosito}. személy összesen {bent_toltott_ido} percet volt bent, a megfigyelés végén a társalgóban volt.")
