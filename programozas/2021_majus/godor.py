# Ladányi Attila

# 1.

lista = []
fajl = open("melyseg.txt", "r", encoding="utf-8")

for sor in fajl:
    sor = int(sor.strip())

    lista.append(sor)

print(f"1. feladat\nA fájl adatainak száma: {len(lista)}")

# 2.

beker_tavolsagertek = int(input("\n2. feladat\nAdjon meg egy távolságértéket! ")) - 1 # -1 az index miatt

print(f"Ezen a helyen a felszín {lista[beker_tavolsagertek]} méter mélyen van.")

# 3.

erintetlen = 0 # azaz hány 0 van a listában

for melyseg in lista:
    if melyseg == 0:
        erintetlen += 1

erintetlen_szazalek = round((erintetlen / len(lista)) * 100, 2)

print(f"\n3. feladat\nAz érintetlen terület aránya {erintetlen_szazalek}%.")

# 4.

godrok = {} # kulcs: gödör kezdetének indexe, érték: a gödör mélységei listában
seged_lista = [] # ebbe rakjuk a mélységeket

for index in range(0, len(lista)):
    jelenlegi_elem = lista[index]

    if jelenlegi_elem == 0: # ha nincs gödör
        if seged_lista != []: # ha a segédben van mélység, azaz előtte gödör volt (ez azért kell, hogy ne legyen tele a szótár []-es értékekkel)
            godrok[index - len(seged_lista)] = seged_lista # index - len(seged_lista): ez a gödör kezdetének sorszáma
            seged_lista = []
    else: # ha gödör van
        seged_lista.append(jelenlegi_elem)

kiir = open("godrok.txt", "w", encoding="utf-8")

for godor in godrok.values(): # azért .values() és nem .items(), mert a kulcsok most nem kellenek
    godor_szovegkent = [str(melyseg) for melyseg in godor] # .join() miatt
    kiir.write(f"{' '.join(godor_szovegkent)}\n")

# 5.

print(f"\n5. feladat\nA gödrök száma: {len(godrok)}")

# 6.

print("\n6. feladat")

if lista[beker_tavolsagertek] == 0:
    print("Az adott helyen nincs gödör.")
else:
    # a.
    print("a)")

    melyik_godor = [] # értéke az a gödör lesz ([kezdet, [melysegek_lista]]), amiben van ez a mélység

    for kezdet, melysegek in godrok.items():
        if kezdet <= beker_tavolsagertek and beker_tavolsagertek <= (kezdet + len(melysegek) - 1): # (kezdet + len(melysegek) - 1) utolsó mélység a gödörben; -1 azért, mert ha nem lenne, akkor a gödör után lévő érintetlen talaj indexe lenne
            melyik_godor = [kezdet, melysegek]

    print(f"A gödör kezdete: {melyik_godor[0] + 1} méter, a gödör vége: {melyik_godor[0] + len(melyik_godor[1])} méter.") # a +1 és a -1 hiánya az index miatt van

    # b.
    print("b)")

    # a megoldásnál felhasználjuk a monotonitás matematikai fogalmát: a gödör mélységeiből kivonjuk az előtte lévőt (ha van) és az eredmény előjelét elmentjük egy listába:
    # +: emelkedik, mivel az előtte lévő kisebb
    # -: mélyül, mivel az előtte lévő nagyobb
    # 0: ugyanannyi a mélység: a jelenlegi és az előtte lévő egyenlő, így a különbség 0: ezt nem vizsgáljuk, mivel nem történhet irányváltozás

    elojel_lista = []

    for index in range(1, len(melyik_godor[1])): # 1, mert a legelső előtt nincs elem
        kulonbseg = melyik_godor[1][index] - melyik_godor[1][index - 1] # a jelenlegiből kivonjuk az előtte lévőt

        if kulonbseg < 0:
            elojel_lista.append("-")
        elif kulonbseg > 0:
            elojel_lista.append("+")

    elojel_valtasok = 0

    if elojel_lista != []: # ha csak ugyanolyan mélységek vannak a listában, akkor biztosan monoton és így csak 0-kal lenne tele de azt nem raktuk bele
        for index in range(1, len(elojel_lista)):
            jelenlegi_elem = elojel_lista[index]
            elotte_levo_elem = elojel_lista[index - 1]

            if jelenlegi_elem != elotte_levo_elem: # ha igaz, akkor változik az előjel, mindegy, hogy (+)-ból (-)-ba vagy fordítva
                elojel_valtasok += 1

    # csakis 0 vagy 1 előjel váltás esetén mélyül folyamatosan a gödör

    if elojel_valtasok <= 1:
        print("Folyamatosan mélyül.")
    else:
        print("Nem mélyül folyamatosan.")

    # c.

    print(f"c)\nA legnagyobb mélysége {max(melyik_godor[1])} méter.")

    # d.

    terfogat = 10 * 1 * sum(melyik_godor[1]) # szélesség * hossz * magasság (olyan magas, amennyi az összmélység; értsd olyan, mintha magassag db 10 * 1 -es téglatesteket raknál egymásra)

    print(f"d)\nA térfogata {terfogat} m^3.")

    # e.

    vizmennyiseg = terfogat - (10 * 1 * len(melyik_godor[1])) # az összesből kiveszek annyi "téglatestet", amennyi a tetején van, azaz len() darabot

    print(f"e)\nA vízmennyiség {vizmennyiseg} m^3.")
