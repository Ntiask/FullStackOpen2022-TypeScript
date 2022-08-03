def hae_aika(osoite, aika):
    nimet = []
    with open(osoite) as tiedosto:
        lista = []
        sisalto = tiedosto.read()
        reseptilista = sisalto.replace("\n\n", ",").split(',')
        for i in reseptilista:
            lista.append(i.replace("\n", ",").split(","))
    
    for i in lista:
        if int(i[1]) < aika:
            nimet.append(f"{i[0]}, valmistusaika {i[1]} min")
    return nimet

loydetyt = hae_aika("reseptit1.txt", 20)

for resepti in loydetyt:
    print(resepti)