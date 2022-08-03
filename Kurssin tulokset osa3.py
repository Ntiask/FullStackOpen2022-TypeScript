from math import trunc

if False:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
    koepisteet = input("koepisteet: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"
    koepisteet = "koepisteet1.csv"

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

kokeet = {}

with open(koepisteet) as tiedosto:
    summa = 0
    for rivi in tiedosto:
        osat = rivi.split(';')
        if osat[0] == "opnro":
            continue
        for i in osat:
            if len(i.strip()) > 3:
                continue
            summa += int(i.strip())
        kokeet[osat[0]]= summa
        summa=0


opiskelijataulu = {}

for opnro, nimi in opiskelijat.items():
    if opnro in tehtavat and opnro in kokeet:
        teht_lkm = tehtavat[opnro]
        tehtavapisteet = trunc(tehtavat[opnro]/4)
        pisteetKokeista = kokeet[opnro]
        arvosanapisteet = tehtavapisteet + pisteetKokeista
        if arvosanapisteet in range(0,15) or arvosanapisteet < 0:
            arvosana = 0
        elif arvosanapisteet in range(15,18):
            arvosana = 1
        elif arvosanapisteet in range(18,20):
            arvosana = 2
        elif arvosanapisteet in range(21,24):
            arvosana = 3
        elif arvosanapisteet in range(24, 28):
            arvosana = 4
        else:
            arvosana = 5
        
        opiskelijataulu[opiskelijat[opnro]] =  [teht_lkm,tehtavapisteet,pisteetKokeista, arvosanapisteet, arvosana]
         
print(f"nimi"," "*25, "teht_lkm",' ', "teht_pist", ' koe_pist', "  ", "yht_pist", " ", "arvosana  ")
for key, value in opiskelijataulu.items():
    print(f"{key:<30} {value[0]:<10} {value[1]:<10} {value[2]:<10} {value[3]:<10} {value[4]:<10}")
