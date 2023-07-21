# Ladányi Attila

# 1.

class Jelentesek:
    def __init__(self, telepules, ido, szelirany_erosseg, homerseklet):
        self.telepules = telepules
        self.ido = ido # stringként meghagyjuk
        self.szelirany_erosseg = szelirany_erosseg
        self.homerseklet = int(homerseklet)

        self.ora = self.ido[0:2] # első két karakter
        self.perc = self.ido[2:] # utolsó két karakter, ha nincs szám a : után/előtt, akkor végig/elejétől nézi, legyen akármennyi karakter bármely irányba

        self.szelerosseg = int(self.szelirany_erosseg[3:])

    def __repr__(self):
        return f"{self.telepules} {self.ido} {self.szelirany_erosseg} {self.homerseklet}"

lista = []

fajl = open("tavirathu13.txt", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Jelentesek(*sor))

# 2.

beker_telepules = input("2. feladat\nAdja meg egy település kódját! Település: ")

beker_telepuleshez_jelentesek = [] # a településhez tartozó jelentések

for jelentes in lista:
    if jelentes.telepules == beker_telepules:
        beker_telepuleshez_jelentesek.append(jelentes)

print(f"Az utolsó mérési adat a megadott településről {beker_telepuleshez_jelentesek[-1].ora}:{beker_telepuleshez_jelentesek[-1].perc}-kor érkezett.") # azért -1. index, mivel időrendben vannak a jelentések

# 3.

homerseklet_szerint_rendezve = sorted(lista, key = lambda jelentes: jelentes.homerseklet) # növekvő sorrendbe rakjuk a jelenetéseket hőmérséklet szerint (amit egy lambda függvénnyel rendelünk az objektumhoz)

print(f"3. feladat\nA legalacsonyabb hőmérséklet: {homerseklet_szerint_rendezve[0].telepules} {homerseklet_szerint_rendezve[0].ora}:{homerseklet_szerint_rendezve[0].perc} {homerseklet_szerint_rendezve[0].homerseklet} fok.")
print(f"A legmagasabb hőmérséklet: {homerseklet_szerint_rendezve[-1].telepules} {homerseklet_szerint_rendezve[-1].ora}:{homerseklet_szerint_rendezve[-1].perc} {homerseklet_szerint_rendezve[-1].homerseklet} fok.")

# 4.

szelcsend_lista = []

for jelentes in lista:
    if jelentes.szelirany_erosseg == "00000":
        szelcsend_lista.append(jelentes)

print("4. feladat")

if len(szelcsend_lista) == 0:
    print("Nem volt szélcsend a mérések idején.")
else:
    for jelentes in szelcsend_lista:
        print(f"{jelentes.telepules} {jelentes.ora}:{jelentes.perc}")

# 5.

varosok_nevei = set() # kiszedjük a városok neveit

for jelentes in lista:
    varosok_nevei.add(jelentes.telepules)

print("5. feladat")

for varos_neve in varosok_nevei:
    kozephomerseklet = "NA" # ez lesz a kezdőérték, ha tudunk számolni középhőmérsékletet, akkor változik majd
    kozephom_orakban = [] # csak a 1., 7., 13., 19 órák hőmérséklete
    homersekletek = [] # az összes hőmérséklet az ingadozás miatt
    kozephom_orai = set() # megnézzük, melyik órákat tartalmazzák a jelentések

    for jelentes in lista:
        if jelentes.telepules == varos_neve:
            if jelentes.ora in ["01", "07", "13", "19"]: # ha a négy óra valamelyike
                kozephom_orakban.append(jelentes.homerseklet)
                kozephom_orai.add(jelentes.ora)

            homersekletek.append(jelentes.homerseklet)

    if len(kozephom_orai) == 4: # ha van négy érték, akkor mind a négy órában volt mérés, minden más esetben marad az "NA"
        kozephomerseklet = int(round(sum(kozephom_orakban) / len(kozephom_orakban), 0))

    hoingas = max(homersekletek) - min(homersekletek)

    if kozephomerseklet == "NA":
        print(f"{varos_neve} NA; Hőmérséklet-ingadozás: {hoingas}")
    else:
        print(f"{varos_neve} Középhőmérséklet: {kozephomerseklet}; Hőmérséklet-ingadozás: {hoingas}")

# 6.

for varos_neve in varosok_nevei:
    kiir = open(f"{varos_neve}.txt", "w", encoding="utf-8") # olyan fálj, aminek a neve "varos_neve.txt"

    kiir.write(f"{varos_neve}\n") # első sor a város neve

    for jelentes in lista:
        if jelentes.telepules == varos_neve:
            kiir.write(f"{jelentes.ora}:{jelentes.perc} {'#' * jelentes.szelerosseg}\n") # annyi '#', amennyi a szélerősség


print("6. feladat\nA fájlok elkészültek.")
