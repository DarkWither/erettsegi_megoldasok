# Ladányi Attila

# 1.

import math

class Zeneszam:
    def __init__(self, sorszam, perc, masodperc, eloado, zenecim):
        self.sorszam = sorszam
        self.perc = int(perc)
        self.masodperc = int(masodperc)
        self.eloado = eloado
        self.zenecim = zenecim

    def __repr__(self):
        return f"{self.eloado} {self.zenecim}"

def formatum(perc, masodperc):
    perc += math.floor(masodperc / 60)
    masodperc -= math.floor(masodperc / 60) * 60

    ora = math.floor(perc / 60)
    perc -= math.floor(perc / 60) * 60

    return [ora, perc, masodperc]


f = open("musor.txt", "r", encoding="utf-8")

lista = []

zeneszamok = int(f.readline())

for i in f:
    jo = []
    nev = []
    i = i.strip().split()

    jo.append(i[0])
    jo.append(i[1])
    jo.append(i[2])

    for j in i:
        if j not in jo:
            nev.append(j)

    ossz = ""

    for i in nev:
        ossz += i + " "

    nev = ossz.split(":")

    if len(nev) > 2:
        nev[1] = nev[1] + ":" + nev[2]
        nev.remove(nev[2])

    nev[1] = list(nev[1])

    nev[1][len(nev[1]) - 1] = ""

    nev[1] = "".join(nev[1])

    lista.append(Zeneszam(*jo, *nev))

# 2.

darab = {}

for i in lista:
    darab[i.sorszam] = darab.get(i.sorszam, 0) + 1

print("2. feladat\nCsatornánként hány zeneszámot lehetett meghallgatni:")

for i, j in darab.items():
    print(f"{i}: {j}")

# 3.

egyes = enumerate([i for i in lista if i.sorszam == "1"])

elso = [0, 0]
utolso = [0, 0]
eloford = [0, 0]

for i in egyes:
    if i[1].eloado != "Eric Clapton":
        elso[0] += i[1].perc
        elso[1] += i[1].masodperc
    else:
        elso[0] += i[1].perc
        elso[1] += i[1].masodperc
        eloford[0] = i[0]
        break

for i in egyes:
    if i[1].eloado == "Eric Clapton":
        eloford[1] = i[0]

egyes = enumerate([i for i in lista if i.sorszam == "1"])

for i in egyes:
    if i[0] == eloford[1]:
        break
    else:
        utolso[0] += i[1].perc
        utolso[1] += i[1].masodperc


hossz = [utolso[0] - elso[0],utolso[1] - elso[1]]

a = formatum(*hossz)

print(f"\n3.feladat\nEltelt idő: {a[0]}:{a[1]}:{a[2]}")

# 4.

szamozott = enumerate([i for i in lista])

omega = [i for i in szamozott if i[1].eloado == "Omega" and i[1].zenecim == "Legenda"]

omegamelyik = omega[0][1].sorszam

lehet = ["1", "2", "3"]

lehet.remove(omegamelyik)

egyik = ""
masik = ""

szamozott = enumerate([i for i in lista])

for i, j in szamozott:
    if i < omega[0][0]:
        if str(j.sorszam) in lehet:
            if j.sorszam == lehet[0]:
                egyik = j
            else:
                masik = j
    else:
        break

print(f"\n4.feladat\nA szám itt volt hallható: {omegamelyik}\nMásik két adón a {egyik.eloado}: {egyik.zenecim} és a {masik.eloado}: {masik.zenecim} ment akkor.")

# 5.

print(f"\n5. feladat")

a = input("Kérem a kiolvasható karaktereket: ")

def olvashato(s, beker):
    van = list(beker)

    s = s.lower()

    szamlalo = 0

    for i in s:
        if i == van[szamlalo]:
            szamlalo += 1
        if szamlalo == len(van):
            break

    return szamlalo == 5

szamozott = enumerate([i for i in lista])

jok = [[i, j] for i, j in szamozott if olvashato(j.eloado + j.zenecim, a)]

f = open("keres.txt", "w", encoding="utf-8")

f.write(f"{a}\n")

for i, j in jok:
    f.write(f"{i}\n")

# 7. feladat

ido = [0, 0, 0]

percek = [0, 0]

ora = 0

egyes = [i for i in lista if i.sorszam == "1"]

percek = [0, 0]

a = [0, 0, 0]

for i in range(len(egyes)):

    if a[0] > ido[0]:
        percek[0] = 0
        percek[1] = 0

        ido[1] = 0
        ido[2] = 0

        ora += 1

        ido[0] = ora
    else:
        # Bevezető
        percek[0] += 1

        percek[0] += egyes[i].perc
        percek[1] += egyes[i].masodperc

        ido[2] += percek[1]
        ido[1] += percek[0]

    try:
        a = formatum(percek[0] + egyes[i + 1].perc, percek[1] + egyes[i + 1].masodperc)
        a[0] += ora
    except IndexError:
        break


kesz = formatum(ido[1], ido[2])
kesz[0] += ido[0]

print(f"\n6. feladat\nEkkor ér véget a módosított adás: {kesz[0]}:{kesz[1]}:{kesz[2]}")
