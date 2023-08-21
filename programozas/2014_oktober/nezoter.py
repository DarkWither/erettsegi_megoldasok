# Ladányi Attila

# 1.

foglaltlista = []
kategorialista = []

for i in open("foglaltsag.txt", "r", encoding = "utf-8"):
    seged = []

    for betu in i.strip():
        seged.append(betu)

    foglaltlista.append(seged)

for i in open("kategoria.txt", "r", encoding = "utf-8"):
    seged = []

    for betu in i.strip():
        seged.append(int(betu))

    kategorialista.append(seged)

# 2.

print("2. feladat")

bekersor = int(input("Kérem a sor számát: "))
bekerszek = int(input("Kérem a szék számát: "))

if foglaltlista[bekersor - 1][bekerszek - 1] == "x":
    print("A szék már foglalt.")
else:
    print("A szék szabad.")

# 3.

hanyjegyet = 0

for i in foglaltlista:
    for j in i:
        if j == "x":
            hanyjegyet += 1

szazalek = int(round((hanyjegyet / (20 * 15)) * 100, 0))

print(f"\n3. feladat\nAz előadásra eddig {hanyjegyet} jegyet adtak el, ez a nézőtér {szazalek}%-a.")

# 4.

tipus = {}

for sor in range(0, 15):
    for szek in range(0, 20):
        if foglaltlista[sor][szek] == "x":
            tipus[kategorialista[sor][szek]] = tipus.get(kategorialista[sor][szek], 0) + 1

legtobb = [0, 0]

for i, j in tipus.items():
    if j > legtobb[1]:
        legtobb[0] = i
        legtobb[1] = j

print(f"\n4. feladat\nA legtöbb jegyet a(z) {legtobb[0]}. árkategóriában értékesítették.")

# 5.

arak = {
    1: 5000,
    2: 4000,
    3: 3000,
    4: 2000,
    5: 1500
}

bevetel = 0

for i, j in tipus.items():
    bevetel += arak[i] * j

print(f"\n5. feladat\nA színház pillanatnyi bevétele {bevetel}Ft.")

# 6.

egyedulallo = 0

for sor in range(0, 15):
    for szek in range(0, 20):
        jelenlegi = foglaltlista[sor][szek]
        elotte = ""
        utana = ""
        try:
            if not szek - 1 == -1:
                elotte = foglaltlista[sor][szek - 1]
            else:
                elotte = "x"
        except IndexError:
            elotte = "x"

        try:
            utana = foglaltlista[sor][szek + 1]
        except IndexError:
            utana = "x"

        if jelenlegi == "o" and (elotte != "o" and utana != "o"):
            egyedulallo += 1


print(f"\n6. feladat\nEgyedülálló üres székek száma: {egyedulallo}")

# 7.

f = open("szabad.txt", "w", encoding="utf-8")

for sor in range(0, 15):
    for szek in range(0, 20):
        if foglaltlista[sor][szek] == "x":
            f.write("x")
        else:
            f.write(f"{kategorialista[sor][szek]}")
    f.write("\n")
