# Ladányi Attila

# 1.

class Jelolt:
    def __init__(self, kerulet, leadott_szavazatok, vezeteknev, utonev, part):
        self.kerulet = int(kerulet)
        self.leadott_szavazatok = int(leadott_szavazatok)
        self.vezeteknev = vezeteknev
        self.utonev = utonev
        self.part = part

    def __repr__(self):
        return f"{self.kerulet} {self.leadott_szavazatok} {self.vezeteknev} {self.utonev} {self.part}"


fajl = open("szavazatok.txt", "r", encoding="utf-8")

lista = []

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Jelolt(*sor))

# 2.

print(f"2. feladat\nA helyhatósági választáson {len(lista)} képviselőjelölt indult.")

# 3.

beker_vezeteknev = input("\n3. feladat\nAdja meg a képviselő vezetéknevét: ")
beker_keresztnev = input("Adja meg a képviselő keresztnevét: ")

szavazatok_szama = -1  # azért -1 és nem 0, mert a -1 lehetetlen, de a 0 lehetséges szavazatszám

for jelolt in lista:
    if jelolt.vezeteknev == beker_vezeteknev and jelolt.utonev == beker_keresztnev:
        szavazatok_szama = jelolt.leadott_szavazatok

if szavazatok_szama == -1:  # ha nem változott az érték, akkor:
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
else:
    print(f"A képviselőjelölt {szavazatok_szama} szavazatot kapott.")

# 4.

osszes_szavazat = 0

for jelolt in lista:
    osszes_szavazat += jelolt.leadott_szavazatok

# a feladatleírásban szerepel, hogy 12345 szavazásra jogosult állampolgár van, ezért:

print(
    f"\n4. feladat\nA választáson {osszes_szavazat} állampolgár, a jogosultak {round((osszes_szavazat / 12345) * 100, 2)}%-a vett részt.")

# 5.

partok_roviditese = {
    "GYEP": "Gyümölcsevők Pártja",
    "HEP": "Húsevők Pártja",
    "TISZ": "Tejivók Szövetsége",
    "ZEP": "Zöldségevők Pártja",
    "-": "Független jelöltek"
}  # könnyebb kiírás végett

szavazatok_partonkent = {}  # kulcs: párt neve, érték: szavazatok száma

for jelolt in lista:
    szavazatok_partonkent[partok_roviditese[jelolt.part]] = szavazatok_partonkent.get(partok_roviditese[jelolt.part], 0) + jelolt.leadott_szavazatok

print("\n5. feladat\nSzavaztok aránya pártonként:")

for part_neve, szavazat in szavazatok_partonkent.items():
    print(f"{part_neve}= {round((szavazat / osszes_szavazat) * 100, 2)}%")

# 6.

legtobb_szavazat = 0  # mennyi volt a legtobb szavazat

for jelolt in lista:
    if jelolt.leadott_szavazatok > legtobb_szavazat:
        legtobb_szavazat = jelolt.leadott_szavazatok

legtobb_szavazat_jeloltek = []  # kik kaptak ennyi szavazatot

for jelolt in lista:
    if jelolt.leadott_szavazatok == legtobb_szavazat:
        legtobb_szavazat_jeloltek.append(jelolt)

print("\n6. feladat\nLegtöbb szavazatot kapott jelöltek:")

for jelolt in legtobb_szavazat_jeloltek:
    if jelolt.part == "-":  # ha független, akkor:
        print(f"{jelolt.vezeteknev} {jelolt.utonev} független")
    else:
        print(f"{jelolt.vezeteknev} {jelolt.utonev} {jelolt.part}")

# 7.

kiir = open("kepviselok.txt", "w", encoding="utf-8")

for kerulet in range(1, 9): # 8 számozott kerület van, lásd feladatleírás első bekezdés
    abban_a_keruletben = [] # mely képviselők indultak abban a kerületben

    for jelolt in lista:
        if jelolt.kerulet == kerulet:
            abban_a_keruletben.append(jelolt)

    legtobb = abban_a_keruletben[0] # az első objektumhoz hasonlítjuk a többit

    for jelolt in abban_a_keruletben:
        if jelolt.leadott_szavazatok > legtobb.leadott_szavazatok:
            legtobb = jelolt

    if legtobb.part == "-":  # ha független, akkor:
        kiir.write(f"{kerulet} {legtobb.vezeteknev} {legtobb.utonev} független\n")
    else:
        kiir.write(f"{kerulet} {legtobb.vezeteknev} {legtobb.utonev} {legtobb.part}\n")
