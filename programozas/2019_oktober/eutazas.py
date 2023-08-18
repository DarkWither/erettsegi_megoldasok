# Ladányi Attila

# 1.

class Utas:
    def __init__(self, megallo, felszallas, azonosito, tipus, ervenyesseg):
        self.ervenyesseg = ervenyesseg
        self.megallo = megallo
        self.felszallas = felszallas
        self.azonosito = azonosito
        self.tipus = tipus

        self.berlete = False

        self.felev = int(self.felszallas[0:4])
        self.felhonap = int(self.felszallas[4:6])
        self.felnap = int(self.felszallas[6:8])

        self.felnapokban = self.felev * 365 + self.felhonap * 30 + self.felnap

        if len(self.ervenyesseg) <= 2:
            self.meddigjo = int(self.ervenyesseg)
        else:
            self.berlete = True
            self.meddigjo = int(self.ervenyesseg[0:4]) * 365 + int(self.ervenyesseg[4:6]) * 30 + int(self.ervenyesseg[6:9])
            self.leev = int(self.ervenyesseg[0:4])
            self.lehonap = int(self.ervenyesseg[4:6])
            self.lenap = int(self.ervenyesseg[6:8])

        # felszálhat-e

        self.nemszallhat = False

        if self.berlete:
            if self.meddigjo - self.felnapokban < 0:
                self.nemszallhat = True

        elif not self.berlete:
            if self.meddigjo == 0:
                self.nemszallhat = True

        # ingyenes vagy kedvezményes

        self.ingyenese = False
        self.kedvezmenyese = False

        if self.tipus in ["NYP", "RVS", "GYK"]:
            self.ingyenese = True

        if self.tipus in ["TAB", "NYB"]:
            self.kedvezmenyese = True

    def __repr__(self):
        return f"{self.meddigjo} {self.felev} {self.felhonap} {self.felnap}"

lista = [Utas(*i.strip().split()) for i in open("utasadat.txt", "r", encoding = "utf-8")]

# 2.

print(f"2. feladat\nA buszra {len(lista)} utas akart felszállni.")

# 3.

lejart = [i for i in lista if i.nemszallhat]

print(f"3. feladat\nA buszra {len(lejart)} utas nem szállhatott fel. ")

# 4.

megallonkent = {}

for i in lista:
    megallonkent[i.megallo] = megallonkent.get(i.megallo, 0) + 1

legnagyobb = ["", 0]

for i, j in megallonkent.items():
    if j > legnagyobb[1]:
        legnagyobb[0] = i
        legnagyobb[1] = j

print(f"4. feladat\nA legtöbb utas ({legnagyobb[1]} fő) a {legnagyobb[0]}. megállóban próbált felszállni.")

# 5.

ingyenesen = len([i for i in lista if i.ingyenese and not i.nemszallhat])
kedvezmenyesen = len([i for i in lista if i.kedvezmenyese and not i.nemszallhat])

print(f"5. feladat\nIngyenesen utazók száma: {ingyenesen} fő\nA kedvezményesen utazók száma: {kedvezmenyesen} fő")

# 6.

def napokszama(e1, h1, n1, e2, h2, n2):
     h1 = (h1 + 9) % 12
     e1 = e1 - h1 // 10
     d1 = 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
     h2 = (h2 + 9) % 12
     e2 = e2 - h2 // 10
     d2 = 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
     return d2-d1

# 7.

f = open("figyelmeztetes.txt", "w", encoding="utf-8")

for i in lista:
    if i.berlete:
        if napokszama(i.felev, i.felhonap, i.felnap, i.leev, i.lehonap, i.lenap) <= 3 and napokszama(i.felev, i.felhonap, i.felnap, i.leev, i.lehonap, i.lenap) >= 1:
            f.write(f"{i.azonosito} {i.leev}-{i.lehonap}-{i.lenap}\n")
