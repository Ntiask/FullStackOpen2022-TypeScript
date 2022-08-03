def hae_nimi(osoite, nimi):
    nimet = []
    with open(osoite) as tiedosto:
        lista = []
        sisalto = tiedosto.read()
        reseptilista = sisalto.replace("\n\n", ",").split(',')
        for i in reseptilista:
            lista.append(i.replace("\n", ",").split(","))
    
    for i in lista:
        if nimi.lower() in i[0].lower():
            nimet.append(i[0])
    return nimet

loydetyt = hae_nimi("reseptit1.txt", "pulla")

for resepti in loydetyt:
    print(resepti)

