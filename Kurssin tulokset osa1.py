

if False:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"

opiskelijat = {}

with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(';')
        if osat[0] == "opnro":
            continue
        opiskelijat[osat[0]] = osat[1]+" "+osat[2].rstrip()

tehtavat = {}

with open(tehtavatiedot) as tiedosto:
    summa = 0
    for rivi in tiedosto:
        osat = rivi.split(';')
        if osat[0] == "opnro":
            continue
        for i in osat:
            if len(i.strip()) > 3:
                continue
            summa += int(i.strip())
        tehtavat[osat[0]]= summa
        summa=0

for opnro, nimi in opiskelijat.items():
    if opnro in tehtavat:
        print(opiskelijat[opnro], tehtavat[opnro])
