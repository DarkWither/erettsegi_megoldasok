# Ladányi Attila

# 1.

beker_szoveg = input("1. feladat\nKérem adjon meg egy szöveget: ")

karakterek = set()

for betu in beker_szoveg:
    karakterek.add(betu)

print(f"A szövegben {len(karakterek)} különböző karakter van, melyek: {', '.join(karakterek)}")

# 2.

fajl = open("szotar.txt", "r", encoding="ASCII") # a feladat ASCII kódolást ír elő

szavak = []

for sor in fajl:
    sor = sor.strip()

    szavak.append(sor)

# 3.

def abcrend(szo):
    # a 'szo' karaktereit ábécérendbe rakja

    return ''.join(sorted(szo))

kiir = open("abc.txt", "w", encoding="utf-8")

for szo in szavak:
    kiir.write(f"{abcrend(szo)}\n")

# 4.

beker_egyik = input("\n4. feladat\nKérek egy szót: ")
beker_masik = input("Kérek egy másik szót: ")

if abcrend(beker_egyik) == abcrend(beker_masik): # azaz ha egymás anagrammái, akkor:
    print("Anagramma")
else:
    print("Nem anagramma")

# 5.

beker_kereses = input("\n5. feladat\nKérek egy szót az anagrammáinak megkereséséhez: ")

anagrammak_kereses = []

for szo in szavak:
    if abcrend(szo) == abcrend(beker_kereses):
        anagrammak_kereses.append(szo)

if len(anagrammak_kereses) == 0:
    print("Nincs a szótárban anagramma")
else:
    print("A szó anagrammái:")
    for szo in anagrammak_kereses:
        print(szo)

# 6.

leghosszabb_karakterszam = 0 # leghosszabb szavak karaktereinek a száma

for szo in szavak:
    if len(szo) > leghosszabb_karakterszam:
        leghosszabb_karakterszam = len(szo)

leghosszabb_szavak = [] # leghosszabb szavakat külön listába

for szo in szavak:
    if len(szo) == leghosszabb_karakterszam:
        leghosszabb_szavak.append(szo)

anagrammankent_csoportositva = {} # leghosszabb szavak anagrammánként csoportosítva; kulcs: betűrendben a szó, érték: szavak sortöréssel elválasztva

for szo in leghosszabb_szavak:
    anagrammankent_csoportositva[abcrend(szo)] = anagrammankent_csoportositva.get(abcrend(szo), "") + f"{szo}\n"

print("\n6. feladat\nLeghosszabb szavak anagrammákként csoportosítva:")

for beturend, szo in anagrammankent_csoportositva.items():
    print(szo)

# 7.

szavak_hosszai = set() # ezek alapján csoportosítjuk majd kiírásnál

for szo in szavak:
    szavak_hosszai.add(len(szo))

rendezett = sorted(list(szavak_hosszai)) # növekvő sorrendben

kiir = open("rendezve.txt", "w", encoding="utf-8")

for hossz in szavak_hosszai:
    adott_hosszuak = [] # 'hossz' hosszúságú szavak

    for szo in szavak:
        if len(szo) == hossz:
            adott_hosszuak.append(szo)

    anagrammankent_csoportositva = {} # lásd 6. feladat

    for szo in adott_hosszuak:
        anagrammankent_csoportositva[abcrend(szo)] = anagrammankent_csoportositva.get(abcrend(szo), "") + f"{szo} "

    for anagram, szo in anagrammankent_csoportositva.items():
        kiir.write(f"{szo}\n")

    kiir.write("\n") # különböző hosszúak elválasztása miatt
