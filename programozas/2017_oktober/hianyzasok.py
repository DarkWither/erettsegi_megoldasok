# Ladányi Attila

# 1.

class Hianyzas:
    def __init__(self, honap, nap, hianyzok_listaja):
        self.honap = int(honap)
        self.nap = int(nap)
        self.hianyzok_listaja = hianyzok_listaja # lista lesz, amiben így szerepelnek a hiányzók: ["Galagonya Alfonz OXXXXXX", "Galagonya Alfonz OXXXXXX", ...]

    def __repr__(self):
        return f"{self.honap} {self.nap} {self.hianyzok_listaja}"

lista = []
fajl= open("naplo.txt", "r", encoding="utf-8")

seged_honap = 0 # ebbe megy a hónap
seged_nap = 0 # ebbe a nap
seged_lista = [] # ebbe mennek a hiányzások

for sor in fajl:
    sor = sor.strip()

    if sor.split()[0] == "#": # felosztanánk a sort és az első eleme "#", akkor a dátumot rögzíti a sor
        if seged_lista != []: # ha nem üres a seged_lista, akkor összeszedtük az összes hiányzót, tehát
            lista.append(Hianyzas(seged_honap, seged_nap, seged_lista))
            seged_honap = int(sor.split()[1])  # ezért egy és kettő: sor.split() --> ["#", "hh", "nn"]
            seged_nap = int(sor.split()[2])
            seged_lista = [] # visszaállítjuk a kezdőértékeket, hogy a következő nap felvételekor ne zavarjon be
        elif seged_lista == []: # ha még nem vettünk fel hiányzást az adott naphoz, akkor először meghatározzuk a hónapot és napot; ez csak a legelső sornál fog lefutni de külön kell rá feltétel
            seged_honap = int(sor.split()[1]) # ezért egy és kettő: sor.split() --> ["#", "hh", "nn"]
            seged_nap = int(sor.split()[2])
    else: # ha nem "#"-tel kezdődik a sor, akkor hiányzót rögzít, tehát hozzáadjuk a seged_lista-hoz
        seged_lista.append(sor)

lista.append(Hianyzas(seged_honap, seged_nap, seged_lista)) # a legutolsót nem adja hozzá a for ciklusban szereplő kód, ezért azt még külön

# 2.

bejegyzesek_szama = 0

for hianyzas in lista:
    bejegyzesek_szama += len(hianyzas.hianyzok_listaja)

print(f"2. feladat\nA naplóban {bejegyzesek_szama} bejegyzés van.")

# 3.

igazolt_orak = 0
igazolatlan_orak = 0

for hianyzas in lista:
    for hianyzo_ember in hianyzas.hianyzok_listaja: # végig a hiányzókon
        for ora in hianyzo_ember.split()[2]: # hianyzo_ember.split() --> ["vnev", "knev", "orak"]
            if ora == "X":
                igazolt_orak += 1
            elif ora == "I":
                igazolatlan_orak += 1

print(f"3. feladat\nAz igazolt hiányzások száma {igazolt_orak}, az igazolatlanoké {igazolatlan_orak} óra.")

# 4.

def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap - 1] + nap) % 7
    return napnev[napsorszam]

# 5.

beker_honap = int(input("5. feladat\nA hónap sorszáma="))
beker_nap = int(input("A nap sorszáma="))

print(f"Azon a napon {hetnapja(beker_honap, beker_nap)} volt.")

# 6.

beker_hetnap = input("6. feladat\nA nap neve=")
beker_ora = int(input("Az óra sorszáma="))

hianyzasok_azokon_a_napokon = 0

for hianyzas in lista:
    if hetnapja(hianyzas.honap, hianyzas.nap) == beker_hetnap:
        for hianyzo_ember in hianyzas.hianyzok_listaja: # végig a hiányzókon
            if hianyzo_ember.split()[2][beker_ora - 1] in ["X", "I"]: # hianyzo_ember.split()[2][beker_ora - 1] a hiányzó óráinak (hianyzo_ember.split()[2]) a bekért órája ([beker_ora - 1]-dik karaktere) hiányzás-e (akár igazolt, akár nem)
                hianyzasok_azokon_a_napokon += 1

print(f"Ekkor összesen {hianyzasok_azokon_a_napokon} óra hiányzás történt.")

# 7.

hianyzasok_szotar = {} # kulcs: diák neve, érték: hiányzások száma

for hianyzas in lista:
    for hianyzo_ember in hianyzas.hianyzok_listaja: # végig a hiányzókon
        hianyzasainak_szama = 0 # a ciklusváltozó hiányzásait segédváltozóba

        for ora in hianyzo_ember.split()[2]:
            if ora in ["X", "I"]:
                hianyzasainak_szama += 1

        nev = hianyzo_ember.split()[0] + " " + hianyzo_ember.split()[1] # a hiányzó ember teljes neve

        hianyzasok_szotar[nev] = hianyzasok_szotar.get(nev, 0) + hianyzasainak_szama

legtobb_hianyzas_ora = max(hianyzasok_szotar.values())
legtobbet_hianyzok_nevei = []

for nev, hianyzasok_szama in hianyzasok_szotar.items():
    if hianyzasok_szama == legtobb_hianyzas_ora:
        legtobbet_hianyzok_nevei.append(nev)

print(f"7. feladat\nA legtöbbet hiányzó tanulók: {' '.join(legtobbet_hianyzok_nevei)}")
