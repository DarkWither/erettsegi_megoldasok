# Ladányi Attila

# 1.

class Tancok:
    def __init__(self, tanc_neve, holgy_neve, ur_neve):
        self.tanc_neve = tanc_neve
        self.holgy_neve = holgy_neve
        self.ur_neve = ur_neve

    def __repr__(self):
        return f"{self.tanc_neve} {self.holgy_neve} {self.ur_neve}"

lista = []

fajl = open("tancrend.txt", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip() # tánc neve
    sor_ketto = fajl.readline().strip() # hölgy neve
    sor_harom = fajl.readline().strip() # úr neve

    lista.append(Tancok(sor, sor_ketto, sor_harom))

# 2.

print(f"2. feladat\nAz elsőként bemutatott tánc neve: {lista[0].tanc_neve}\nAz utoljára bemutatott tánc neve: {lista[-1].tanc_neve}")

# 3.

samba_hanyszor = 0

for tanc in lista:
    if tanc.tanc_neve == "samba":
        samba_hanyszor += 1

print(f"3. feladat\nÖsszesen {samba_hanyszor} pár mutatott be sambát.")

# 4.

print("4. feladat\nVilma táncai:")

for tanc in lista:
    if tanc.holgy_neve == "Vilma":
        print(tanc.tanc_neve)

# 5.

beker_tancnev = input("5. feladat\nAdja meg egy tánc nevét: ")

vilma_kivel_tancolta = 0 # az objektum lesz az értéke, ha létezik

for tanc in lista:
    if tanc.holgy_neve == "Vilma" and tanc.tanc_neve == beker_tancnev:
        vilma_kivel_tancolta = tanc

if vilma_kivel_tancolta == 0: # ha nem változott az értéke, akkor
    print(f"Vilma nem táncolt {beker_tancnev}-t.")
else:
    print(f"A {beker_tancnev} bemutatóján Vilma párja {vilma_kivel_tancolta.ur_neve} volt.")

# 6.

holgyek_nevei = set()
urak_nevei = set()

for tanc in lista:
    holgyek_nevei.add(tanc.holgy_neve)
    urak_nevei.add(tanc.ur_neve)

kiir = open("szereplok.txt", "w", encoding="utf-8")

kiir.write(f"Lányok: {', '.join(list(holgyek_nevei))}\n")
kiir.write(f"Fiúk: {', '.join(list(urak_nevei))}")

# 7.

holgyek_hanyszor = {} # kulcs: hölgy neve, érték: hányszor táncolt
urak_hanyszor = {} # kulcs: úr neve, érték: hányszor táncolt

for tanc in lista:
    holgyek_hanyszor[tanc.holgy_neve] = holgyek_hanyszor.get(tanc.holgy_neve, 0) + 1
    urak_hanyszor[tanc.ur_neve] = urak_hanyszor.get(tanc.ur_neve, 0) + 1

legtobbet_tancolt_holgyek_nevei = []
legtobbet_tancolt_urak_nevei = []

for nev, hanyszor in holgyek_hanyszor.items():
    if hanyszor == max(holgyek_hanyszor.values()):
        legtobbet_tancolt_holgyek_nevei.append(nev)

for nev, hanyszor in urak_hanyszor.items():
    if hanyszor == max(urak_hanyszor.values()):
        legtobbet_tancolt_urak_nevei.append(nev)

print(f"7. feladat\nLegtöbbet táncolt lányok nevei: {', '.join(legtobbet_tancolt_holgyek_nevei)}")
print(f"Legtöbbet táncolt fiúk nevei: {', '.join(legtobbet_tancolt_urak_nevei)}")
