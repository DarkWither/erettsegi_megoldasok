# Ladányi Attila

# 1.

class Jarmu:
    def __init__(self, rendszam, kezdet_ora, kezdet_perc, kezdet_mperc_egeszresz, kezdet_mperc_ezredek, vege_ora, vege_perc, vege_mperc_egeszresz, vege_mperc_ezredek):
        self.rendszam = rendszam
        self.kezdet_ora = int(kezdet_ora)
        self.kezdet_perc = int(kezdet_perc)
        self.kezdet_mperc_egeszresz = int(kezdet_mperc_egeszresz)
        self.kezdet_mperc_ezredek = int(kezdet_mperc_ezredek)
        self.vege_ora = int(vege_ora)
        self.vege_perc = int(vege_perc)
        self.vege_mperc_egeszresz = int(vege_mperc_egeszresz)
        self.vege_mperc_ezredek = int(vege_mperc_ezredek)

        self.kezdet_oraban = self.kezdet_ora + (self.kezdet_perc / 60) + (self.kezdet_mperc_egeszresz / 3600) + ((self.kezdet_mperc_ezredek / 1000) / 3600) # az ezredet elosztjuk ezerrel, hogy 0,... alakban legyen (így ez is mp lesz) és ezt átváltjuk órába
        self.vege_oraban = self.vege_ora + (self.vege_perc / 60) + (self.vege_mperc_egeszresz / 3600) + ((self.vege_mperc_ezredek / 1000) / 3600)

        self.atlagsebesseg = 10 / (self.vege_oraban - self.kezdet_oraban) # self.vege_oraban - self.kezdet_oraban: a megtételhez szükséges idő

    def __repr__(self):
        return f"{self.rendszam} {self.kezdet_ora} {self.kezdet_perc} {self.kezdet_mperc_egeszresz} {self.kezdet_mperc_ezredek} {self.vege_ora} {self.vege_perc} {self.vege_mperc_egeszresz} {self.vege_mperc_ezredek}"

lista = []

fajl = open("meresek.txt", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Jarmu(*sor))

# 2.

print(f"2. feladat\nA mérés során {len(lista)} jármű adatait rögzítették.")

# 3.

hany_jarmu_kilenc_elott = 0 # az a jármű haladt el 9 előtt, amelyek vege_ora-ja kisebb, mint 9

for jarmu in lista:
    if jarmu.vege_ora < 9:
        hany_jarmu_kilenc_elott += 1

print(f"\n3. feladat\n9 óra előtt {hany_jarmu_kilenc_elott} jármű haladt el a végponti mérőnél.")

# 4.

beker_idopont = input(f"\n4. feladat\nAdjon meg egy óra és perc értéket! ").split() # ["óra", "perc"]

# a.

elhaladt_jarmuvek = 0 # a bekért időpontban hány jármű haladt el

for jarmu in lista:
    if jarmu.kezdet_ora == int(beker_idopont[0]) and jarmu.kezdet_perc == int(beker_idopont[1]): # kezdeti óra és perc egyezzen meg a bekérttel
        elhaladt_jarmuvek += 1

print(f"\ta. A kezdeti méréspontnál elhaladt járművek száma: {elhaladt_jarmuvek}") # tabulátor a minta miatt

# b.

hanyan_voltak_az_utszakaszon = 0
beker_idopont_oraban = int(beker_idopont[0]) + (int(beker_idopont[1]) / 60) # óra + (perc / 60)
beker_idopont_vege = beker_idopont_oraban + (59.999 / 3600) # mikor van vége az időpont percének; a másodpercek (59.999 / 3600) átváltása órába és hozzáadása a bekert időponthoz

for jarmu in lista:
    if jarmu.kezdet_oraban < beker_idopont_oraban: # ha az időpont előtt kezdődik
        if jarmu.vege_oraban >= beker_idopont_oraban: # ha továbbá a kezdet után lesz vége az elhaladásnak akkor
            hanyan_voltak_az_utszakaszon += 1
    elif jarmu.kezdet_oraban >= beker_idopont_oraban and jarmu.kezdet_oraban <= beker_idopont_vege: # ha az időpontban kezdi az áthaladást, biztosan rajta van az elhaladás végétől függetlenül
        hanyan_voltak_az_utszakaszon += 1

forgalom_suruseg = round(hanyan_voltak_az_utszakaszon / 10, 1) # /10 mert 10km az útszakasz

print(f"\tb. A forgalomsűrűség: {forgalom_suruseg}")

# 5.

leggyorsabb_jarmu = lista[0] # az első jármű lesz a kezdőérték

for jarmu in lista:
    if jarmu.atlagsebesseg > leggyorsabb_jarmu.atlagsebesseg: # ha nagyobb, akkor ezután ez lesz a legnagyobb
        leggyorsabb_jarmu = jarmu

lehagyott_jarmuvek_szama = 0

# akkor hagyott le egy járművet, ha a hamarabb vagy ugyanakkor indult el a szakaszon az autó, mint a leggyorsabb, de mire végetért az kisebb, mint a leggyorsabb vége

for jarmu in lista:
    if jarmu.kezdet_oraban <= leggyorsabb_jarmu.kezdet_oraban and jarmu.vege_oraban > leggyorsabb_jarmu.vege_oraban:
        lehagyott_jarmuvek_szama += 1

print("\n5. feladat\nA legnagyobb sebességgel haladó jármű")
print(f"\trendszáma: {leggyorsabb_jarmu.rendszam}")
print(f"\tátlagsebessége: {int(leggyorsabb_jarmu.atlagsebesseg)} km/h")
print(f"\táltal lehagyott járművek száma: {lehagyott_jarmuvek_szama}")

# 6.

gyorshajtok_szama = 0

for jarmu in lista:
    if jarmu.atlagsebesseg > 90:
        gyorshajtok_szama += 1

gyorshajtok_szazalekban = round((gyorshajtok_szama / len(lista)) * 100, 2)

print(f"\n6. feladat\nA járművek {gyorshajtok_szazalekban}%-a volt gyorshajtó.")

# 7.

def buntetes(sebesseg):
    # sebességhez hozzárendeli a büntetést

    visszateresi_ertek = 0

    if sebesseg > 104 and sebesseg <= 121:
        visszateresi_ertek = 30000
    elif sebesseg > 121 and sebesseg <= 136:
        visszateresi_ertek = 45000
    elif sebesseg > 136 and sebesseg <= 151:
        visszateresi_ertek = 60000
    elif sebesseg > 151:
        visszateresi_ertek = 200000

    return visszateresi_ertek

kiir = open("buntetes.txt", "w", encoding="utf-8")

for jarmu in lista:
    if jarmu.atlagsebesseg > 104: # ha büntethető
        kiir.write(f"{jarmu.rendszam}\t{int(jarmu.atlagsebesseg)} km/h\t{buntetes(jarmu.atlagsebesseg)} Ft\n") # a fájl adataiban kerekítési hiba lesz, ezt sem az int(), sem a round() nem tudja orvosolni

print("\nA fájl elkészült.")
