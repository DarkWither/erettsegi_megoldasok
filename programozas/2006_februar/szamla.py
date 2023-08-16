# Ladányi Attila

# 3.
import math


class Hivasok:
    def __init__(self, kezd_ora, kezd_perc, kezd_mperc, veg_ora, veg_perc, veg_mperc, telefonszam):
        self.kezd_ora = int(kezd_ora)
        self.kezd_perc = int(kezd_perc)
        self.kezd_mperc = int(kezd_mperc)
        self.veg_ora = int(veg_ora)
        self.veg_perc = int(veg_perc)
        self.veg_mperc = int(veg_mperc)
        self.telefonszam = int(telefonszam)

        kezdes_masodpercekben = self.kezd_ora * 3600 + self.kezd_perc * 60 + self.kezd_mperc
        veg_masodpercekben =  self.veg_ora * 3600 + self.veg_perc * 60 + self.veg_mperc

        self.hivas_hossza = math.ceil((veg_masodpercekben - kezdes_masodpercekben) / 60)

        self.csucsidoben = False

        if kezdes_masodpercekben >= (7 * 3600) and kezdes_masodpercekben <= (18 * 3600):
            self.csucsidoben = True

        self.mobil = False

        if str(self.telefonszam)[0:2] in ["39", "41", "71"]:
            self.mobil = True
    def __repr__(self):
        return f"{self.kezd_ora} {self.kezd_perc} {self.kezd_mperc} {self.veg_ora} {self.veg_perc} {self.veg_mperc} {self.telefonszam}"

lista=[]
fajl=open("hivasok.txt","r", encoding="utf-8")

for sor in fajl:
    sor=sor.strip().split()
    sor2=fajl.readline().strip()
    lista.append(Hivasok(*sor, int(sor2)))

# 1.

beker_telefonszam = input("1. feladat Adjon meg egy telefonszámot: ")

if beker_telefonszam[0:2] in ["39", "41", "71"]:
    print("Mobiltelefon")
else:
    print("Vezetékes telefon")

# 2.

kezdet_idopont = input("2. feladat Adjon meg egy kezdeti időpontot: ").split()
vege_idopont = input("Adja meg a telefonálás végének időpontját: ").split()

kezdet_masodpercben = int(kezdet_idopont[0]) * 3600 + int(kezdet_idopont[1]) * 60 + int(kezdet_idopont[2])
vege_masodpercben = int(vege_idopont[0]) * 3600 + int(vege_idopont[1]) * 60 + int(vege_idopont[2])

kulonbseg_masodpercben = math.ceil((vege_masodpercben - kezdet_masodpercben) / 60)

print(f"Számlázás szempontjából a beszélgetés {kulonbseg_masodpercben} perces volt.")

# 3.

kiir = open("percek.txt", "w", encoding="utf-8")

for hivas in lista:
    kiir.write(f"{hivas.hivas_hossza} {hivas.telefonszam}\n")

# 4.

csucsidoben_darab = 0
csucsidon_kivul_darab = 0

for hivas in lista:
    if hivas.csucsidoben:
        csucsidoben_darab += 1
    else:
        csucsidon_kivul_darab += 1

print(f"4. feladat\nHívások csúcsidőben: {csucsidoben_darab} db\nHívások csúcsidőn kívül: {csucsidon_kivul_darab} db")

# 5.

hany_percet_mobillal = 0
hany_percet_vezetekessel = 0

for hivas in lista:
    if hivas.mobil:
        hany_percet_mobillal += hivas.hivas_hossza
    else:
        hany_percet_vezetekessel += hivas.hivas_hossza

print(f"5. feladat\nMobillal: {hany_percet_mobillal} perc\nVezetékessel: {hany_percet_vezetekessel} perc")

# 6.

csucsdijasert_fizetendo = 0

for hivas in lista:
    if hivas.csucsidoben:
        if hivas.mobil:
            csucsdijasert_fizetendo += hivas.hivas_hossza * 69.175
        else:
            csucsdijasert_fizetendo += hivas.hivas_hossza * 30

print(f"6. feladat\nCsúcsdíjas hívásokért fizetendő: {int(round(csucsdijasert_fizetendo, 0))} Ft")
